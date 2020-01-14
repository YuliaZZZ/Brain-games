#!/usr/bin/env python3
from brain_games.games.calc import calc
from .brain_games import greeting, welcome_calc
from brain_games.cli import run

def main():
    greeting()
    welcome_calc()
    run()
    calc()


if __name__ == '__main__':
    main()
