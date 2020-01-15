#!/usr/bin/env python3
import random
from operator import sub, mul


def calc(x):
    di = {
       1: [random.randint(1, 10), random.randint(1, 10)],
       2: [random.randint(1, 10), random.randint(1, 10)],
       3: [random.randint(1, 10), random.randint(1, 10)]
       }
    count = 0
    i = 1
    while i <= 3:
        operation = {
                  '{} + {}'.format(di[i][0], di[i][1]): sum(di[i]),
                  '{} - {}'.format(di[i][0], di[i][1]):
                  sub(di[i][0], di[i][1]),
                  '{} * {}'.format(di[i][0], di[i][1]): mul(di[i][0], di[i][1])
                  }
        v = random.choice(list(operation.keys()))
        print("""Question: {}
Your answer: """.format(v), end='')
        answer = input()
        if answer == str(operation[v]):
            count += 1
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}""".format(answer, operation[v], x))
            break
        i += 1
    if count == 3:
        print('Congratulations, {}'.format(x))
        print('')
