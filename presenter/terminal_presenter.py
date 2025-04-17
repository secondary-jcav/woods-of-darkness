import time
import os
from clint.textui import prompt, puts, colored
from typing import Dict, List
from pyfiglet import Figlet

from presenter.presenters import Presenter
from models.entities import Choice


class TerminalPresenter(Presenter):
    def __init__(self, clear_screen: bool = True, typing_delay: float = 0.5):
        self.clear_screen = clear_screen
        self.typing_delay = typing_delay

    def _clear(self) -> None:
        if self.clear_screen:
            os.system('cls' if os.name == 'nt' else 'clear')

    def display_intro_title(self) -> None:
        f = Figlet(font='slant')
        puts(colored.red(f.renderText('The Woods of Darkness')))
        time.sleep(3)

    def display_text(self, text: str) -> None:
        self._clear()
        for line in text.splitlines():
            print(line)
            if self.typing_delay:
                time.sleep(self.typing_delay)
        print()  # blank line after narrative

    def display_choices(self, choices: Dict[str, Choice]) -> None:
        for key, choice in choices.items():
            print(f"  [{key}] {choice.description}")
        print()

    def get_choice(self, valid_keys: List[str]) -> str:
        while True:
            choice = str(prompt.options("Your choice:", valid_keys))
            if choice in valid_keys:
                return choice
            print(f"  ❗️ Invalid choice: {choice!r}. Please pick one of {valid_keys}.")
