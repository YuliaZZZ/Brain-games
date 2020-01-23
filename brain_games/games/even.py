#!/usr/bin/env python3
from random import randint


def is_even(x):
    return 'yes' if x % 2 == 0 else 'no'


def even():
    question = randint(1, 1000)
    return [question, is_even(question)]
