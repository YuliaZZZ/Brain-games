#!/usr/bin/env python3
from .cli import run
import prompt


def engine(func):
    name = run(func)
    counter = 0
    i = 1
    while i <= 3:
        x = func()
        print('Question: {}'.format(x[0]))
        answer = prompt.string('Your answer: ')
        if answer == x[1]:
            counter += 1
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}!""".format(answer, x[1], name))
            break
        i += 1
        if counter == 3:
            print('Congratulations, {}!'.format(name))
