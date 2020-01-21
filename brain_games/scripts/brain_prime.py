#!/usr/bin/env python3
from brain_games.games.prime import prime, is_prime
from brain_games.games.brain import brain
from .brain_games import greeting, welcome_prime
from brain_games.cli import run


def main():
    greeting()
    welcome_prime()
    name = run()
    prime(name, brain, is_prime)


if __name__ == '__main__':
    main()
