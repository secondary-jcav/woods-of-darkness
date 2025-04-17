from typing import Dict
from models.entities import Scene


class GameEngine:
    def __init__(self,
                 scenes: Dict[str, Scene],
                 start_scene: str,
                 presenter):
        self.scenes = scenes
        self.current = start_scene
        self.presenter = presenter

    def run(self) -> None:
        self.presenter.display_intro_title()
        while self.current is not None:
            scene = self.scenes[self.current]

            # 1) DISPLAY
            self.presenter.display_text(scene.text)
            self.presenter.display_choices(scene.choices)

            # 2) INPUT
            pick = self.presenter.get_choice(list(scene.choices.keys()))

            # 3) TRANSITION
            self.current = scene.choices[pick].next_scene

        self.presenter.display_text("=== The End ===")
