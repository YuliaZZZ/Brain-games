#!/usr/bin/env python3
import random
import prompt


def even(x):
    def is_even(x):
        return 'yes' if x % 2 == 0 else 'no'
    di = {
       1: random.randint(1, 10),
       2: random.randint(1, 100),
       3: random.randint(1, 1000)
       }
    count = 0
    i = 1
    while i <= 3:
        print('Question: {}'.format(di.get(i)))
        answer = prompt.string('Your answer: ')
        if answer == is_even(di.get(i)):
            count += 1
            print('Correct!')
        else:
            print("""'yes' is wrong answer :(. Correct answer was 'no'.
Let's try again, {}!""".format(x))
            break
        i += 1
    if count == 3:
        print('Congratulations, {}!'.format(x))
        print('')
