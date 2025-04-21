# The Woods of Darkness

## Description

Choose your own adventure using the command line interface. Built with python, run from main.py

Follows the Clean Architecture model where dependencies only point inwards:

- main.py works is the initial entrypoint of the system; it loads the story, starts the presenter and hands off control to the game engine.
- terminal_presenter.py handles the cli
- engine.py traverses the story, divided in scenes, according to the user's choices.
- entities.py describes the scene models
