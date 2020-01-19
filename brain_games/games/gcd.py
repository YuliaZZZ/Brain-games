#!/usr/bin/env python3
import random
from math import gcd
import prompt


def is_nod(x):
    a, b = x
    return gcd(a, b)


def is_gcd(name):
    di = {
       1: [random.randint(1, 100), random.randint(1, 10)],
       2: [random.randint(1, 100), random.randint(1, 10)],
       3: [random.randint(1, 100), random.randint(1, 10)]
       }
    count = 0
    i = 1
    while i <= 3:
        print('Question: {} {}'.format(di[i][0], di[i][1]))
        answer = prompt.string('Your answer: ')
        if answer == str(is_nod(di[i])):
            count += 1
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}!""".format(answer, is_nod(di[i]), name))
            break
        i += 1
        if count == 3:
            print('Congratulations, {}!'.format(name))
