#!/usr/bin/env python3
from brain_games.games.prime import prime
from brain_games.games.brain import engine
from .brain_games import greeting, welcome_prime
from brain_games.cli import run


def main():
    greeting()
    welcome_prime()
    name = run()
    engine(name, prime)


if __name__ == '__main__':
    main()
