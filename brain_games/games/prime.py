from random import randint
from math import gcd


def prime_check(n):
    if n <= 1:
        return False
    i = n
    rez = 0
    while i >= 1:
        rez = gcd(n, i)
        if 1 < rez < n:
            return 'no'
        i -= 1
    return 'yes'


welcome = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def func():
    question = randint(1, 3000)
    answer = prime_check(question)
    return question, answer
