#!/usr/bin/env python3
from brain_games.cli import run
from .brain_games import greeting, welcome_even
from brain_games.games.even import even, is_even
from brain_games.games.brain import brain


def main():
    greeting()
    welcome_even()
    name = run()
    even(name, brain, is_even)


if __name__ == '__main__':
    main()
