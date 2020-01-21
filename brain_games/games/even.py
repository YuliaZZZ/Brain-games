#!/usr/bin/env python3
import random
import prompt


def is_even(x):
    return 'yes' if x % 2 == 0 else 'no'


items = {
      1: random.randint(1, 10),
      2: random.randint(1, 100),
      3: random.randint(1, 1000)
      }


def even(name):
    counter = 0
    i = 1
    while i <= 3:
        print('Question: {}'.format(items.get(i)))
        answer = prompt.string('Your answer: ')
        if answer == is_even(items.get(i)):
            counter += 1
            print('Correct!')
        else:
            print("""'yes' is wrong answer :(. Correct answer was 'no'.
Let's try again, {}!""".format(name))
            break
        i += 1
    if counter == 3:
        print('Congratulations, {}!'.format(name))
        print('')
