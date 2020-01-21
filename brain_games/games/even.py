#!/usr/bin/env python3
from random import randint


def is_even(x):
    return 'yes' if x % 2 == 0 else 'no'


items = {1: randint(1, 10), 2: randint(1, 100), 3: randint(1, 1000)}


def even(name, func, func2):
    return func(name, func2)
