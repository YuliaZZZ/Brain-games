#!/usr/bin/env python3
from random import randint
from itertools import islice, count


def make_progression():
    z = randint(0, 9)
    progress = list(islice(count(randint(1, 10), randint(1, 10)), 10))
    y = progress[z]
    progress[z] = '..'
    a, a1, a2, a3, a4, a5, a6, a7, a8, a9 = progress
    progression = (
            '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.
            format(a, a1, a2, a3, a4, a5, a6, a7, a8, a9))
    print(progression)
    return str(y)


def progres(name):
    counter = 0
    i = 1
    while i <= 3:
        print("Question: ", end='')
        question = make_progression()
        print('Your answer: ', end='')
        answer = input()
        if answer == question:
            counter += 1
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}!""".format(answer, question, name))
            break
        i += 1
    if counter == 3:
        print('Congratulations, {}!'.format(name))
