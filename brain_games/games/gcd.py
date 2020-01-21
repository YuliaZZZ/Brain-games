#!/usr/bin/env python3
from random import randint
from math import gcd
import prompt


def is_nod(x):
    a, b = x
    return gcd(a, b)


items = {
      1: [randint(1, 100), randint(1, 10)],
      2: [randint(1, 100), randint(1, 10)],
      3: [randint(1, 100), randint(1, 10)]
      }


def is_gcd(name):
    counter = 0
    i = 1
    while i <= 3:
        print('Question: {} {}'.format(items[i][0], items[i][1]))
        answer = prompt.string('Your answer: ')
        if answer == str(is_nod(items[i])):
            counter += 1
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}!""".format(answer, is_nod(items[i]), name))
            break
        i += 1
        if counter == 3:
            print('Congratulations, {}!'.format(name))
