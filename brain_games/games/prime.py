#!/usr/bin/env python3
from random import randint
from math import gcd
import prompt


def is_prime(n):
    if n <= 1:
        return False
    i = n
    rez = 0
    while i >= 1:
        rez = gcd(n, i)
        if 1 < rez < n:
            return 'no'
            break
        i -= 1
    return 'yes'


def prime(name):
    items = {1: randint(1, 3000), 2: randint(1, 3000), 3: randint(1, 3000)}
    counter = 0
    i = 1
    while i <= 3:
        print('Question: {}'.format(items[i]))
        answer = prompt.string('Your answer: ')
        if answer == is_prime(items[i]):
            counter += 1
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}!""".format(answer, is_prime(items[i]), name))
            break
        i += 1
        if counter == 3:
            print('Congratulations, {}!'.format(name))
