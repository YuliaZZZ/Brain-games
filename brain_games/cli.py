#!/usr/bin/env python3
import prompt


def run():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('')
    return name


named = run()


def main():
    run()


if __name__ == '__main__':
    main()
