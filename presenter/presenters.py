from abc import ABC, abstractmethod
from typing import Dict, List
from models.entities import Choice


class Presenter(ABC):
    """
    Defines the minimal contract for any presentation layer.
    The GameEngine relies on these three methods to show text,
    show choices, and get user input.
    """

    @abstractmethod
    def display_text(self, text: str) -> None:
        """
        Render a block of narrative text to the user.
        e.g. print it to the console, show in a GUI textbox, etc.
        """
        ...

    @abstractmethod
    def display_intro_title(self) -> None:
        """
        Welcomes the user.
        """
        ...

    @abstractmethod
    def display_choices(self, choices: Dict[str, Choice]) -> None:
        """
        Render the available choices.

        `choices` is a mapping from the key the user must enter
        (e.g. "1", "a") to a Choice(description, next_scene).
        """
        ...

    @abstractmethod
    def get_choice(self, valid_keys: List[str]) -> str:
        """
        Query the user for one of the valid_keys and return their selection.
        Should loop/re‑prompt on invalid input.
        """
        ...
