#!/usr/bin/env python3
import random
from operator import sub, mul
import prompt


def calc(name):
    items = {
       1: [random.randint(1, 10), random.randint(1, 10)],
       2: [random.randint(1, 10), random.randint(1, 10)],
       3: [random.randint(1, 10), random.randint(1, 10)]
       }
    counter = 0
    i = 1
    while i <= 3:
        operations = {
                  '{} + {}'.format(items[i][0], items[i][1]): sum(items[i]),
                  '{} - {}'.format(items[i][0], items[i][1]):
                  sub(items[i][0], items[i][1]),
                  '{} * {}'.format(items[i][0], items[i][1]):
                  mul(items[i][0], items[i][1])
                  }
        сhoice_operator = random.choice(list(operations.keys()))
        print('Question: {}'.format(сhoice_operator))
        answer = prompt.string('Your answer: ')
        if answer == str(operations[сhoice_operator]):
            counter += 1
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}!""".format(answer, operations[сhoice_operator], name))
            break
        i += 1
    if counter == 3:
        print('Congratulations, {}!'.format(name))
        print('')
