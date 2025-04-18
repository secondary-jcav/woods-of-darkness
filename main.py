from engine.engine import GameEngine
from presenter.terminal_presenter import TerminalPresenter
from drivers.yaml_loader import load_all_chapters


def main() -> None:
    all_scenes = load_all_chapters("chapters")
    presenter = TerminalPresenter()
    game = GameEngine(all_scenes, start_scene="intro.start", presenter=presenter)
    game.run()


if __name__ == "__main__":
    main()
