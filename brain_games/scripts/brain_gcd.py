#!/usr/bin/env python3
from brain_games import games, engine


def main():
    engine.engine(games.gcd.is_gcd)


if __name__ == '__main__':
    main()
