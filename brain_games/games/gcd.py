#!/usr/bin/env python3
import random


def is_gcd(x):
    a, b = x
    i = a
    while i >= 1:
        if b % i == 0 and a % i == 0:
            return i
        i -= 1


def gcd(name):
    di = {
       1: [random.randint(1, 100), random.randint(1, 10)],
       2: [random.randint(1, 100), random.randint(1, 10)],
       3: [random.randint(1, 100), random.randint(1, 10)]
       }
    count = 0
    i = 1
    while i <= 3:
        print("""Question: {} {}
Your answer: """.format(di[i][0], di[i][1]), end='')
        answer = input()
        if answer == str(is_gcd(di[i])):
            count += 1
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}!""".format(answer, is_gcd(di[i]), name))
            break
        i += 1
        if count == 3:
            print('Congratulations, {}!'.format(name))
