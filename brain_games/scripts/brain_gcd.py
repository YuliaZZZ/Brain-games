#!/usr/bin/env python3
from brain_games.games.gcd import is_gcd
from .brain_games import greeting, welcome_gcd
from brain_games.cli import run
from brain_games.games.brain import engine


def main():
    greeting()
    welcome_gcd()
    name = run()
    engine(name, is_gcd)


if __name__ == '__main__':
    main()
