#!/usr/bin/env python3
from brain_games.cli import run
from .brain_games import greeting, welcome_progres
from brain_games.games.progres import progres


def main():
    greeting()
    welcome_progres()
    name = run()
    progres(name)


if __name__ == '__main__':
    main()
