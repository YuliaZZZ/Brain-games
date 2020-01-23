#!/usr/bin/env python3
from brain_games.games.calc import calc
from .brain_games import greeting, welcome_calc
from brain_games.cli import run
from brain_games.games.brain import engine


def main():
    greeting()
    welcome_calc()
    name = run()
    engine(name, calc)


if __name__ == '__main__':
    main()
