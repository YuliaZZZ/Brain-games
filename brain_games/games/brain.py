#!/usr/bin/env python3
import prompt
from .prime import items


def brain(name, func):
    counter = 0
    i = 1
    while i <= 3:
        print('Question: {}'.format(items[i]))
        answer = prompt.string('Your answer: ')
        if answer == func(items[i]):
            counter += 1
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}!""".format(answer, func(items[i]), name))
            break
        i += 1
        if counter == 3:
            print('Congratulations, {}!'.format(name))
