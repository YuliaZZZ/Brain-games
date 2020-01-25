#!/usr/bin/env python3
import prompt


def run(func):
    print('Welcome to the Brain Games!')
    print(func()[2])
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('')
    return name


def main():
    run()


if __name__ == '__main__':
    main()
