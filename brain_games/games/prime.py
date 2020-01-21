#!/usr/bin/env python3
from random import randint
from math import gcd
import prompt


def is_prime(n):
    if n <= 1:
        return False
    i = n
    rez = 0
    while i >= 1:
        rez = gcd(n, i)
        if 1 < rez < n:
            return 'no'
            break
        i -= 1
    return 'yes'


items = {1: randint(1, 3000), 2: randint(1, 3000), 3: randint(1, 3000)}


def prime(name, func, func2):
    return func(name, func2)
