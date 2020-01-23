#!/usr/bin/env python3
from random import randint
from itertools import islice, count


def progression():
    number = randint(0, 9)
    progression = list(islice(count(randint(1, 10), randint(1, 10)), 10))
    secret_elem = progression[number]
    progression[number] = '..'
    a, a1, a2, a3, a4, a5, a6, a7, a8, a9 = progression
    question = (
            '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.
            format(a, a1, a2, a3, a4, a5, a6, a7, a8, a9))
    return [question, str(secret_elem)]
