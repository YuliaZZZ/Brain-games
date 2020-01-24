#!/usr/bin/env python3
from brain_games.games.gcd import is_gcd
from brain_games.engine import engine


def main():
    engine(is_gcd)


if __name__ == '__main__':
    main()
