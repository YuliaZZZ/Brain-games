#!/usr/bin/env python3
from random import randint
from math import gcd


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


def prime():
    question = randint(1, 3000)
    return [question, is_prime(question)]
