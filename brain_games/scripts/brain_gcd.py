#!/usr/bin/env python3
from brain_games.games.gcd import gcd
from .brain_games import greeting, welcome_gcd
from brain_games.cli import run


def main():
    greeting()
    welcome_gcd()
    name = run()
    gcd(name)


if __name__ == '__main__':
    main()
