#!/usr/bin/env python3
from random import randint
from math import gcd


def is_nod(x):
    a, b = x
    return gcd(a, b)


def is_gcd():
    items = [randint(1, 100), randint(1, 100)]
    question = '{} {}'.format(items[0], items[1])
    return [question, str(is_nod(items))]
