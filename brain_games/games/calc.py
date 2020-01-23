#!/usr/bin/env python3
from random import randint, choice
from operator import sub, mul


def calc():
    items = [randint(1, 10), randint(1, 10)]
    operations = {
               '{} + {}'.format(items[0], items[1]): sum(items),
               '{} - {}'.format(items[0], items[1]): sub(items[0], items[1]),
               '{} * {}'.format(items[0], items[1]): mul(items[0], items[1])
                }
    сhoice_operator = choice(list(operations.keys()))
    return [сhoice_operator, str(operations[сhoice_operator])]
