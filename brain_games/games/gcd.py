from random import randint


WELCOME = 'Find the greatest common divisor of given numbers.'


def gcd_check(x, y):
    s = [x, y]
    s.sort()
    a, b = s
    if b % a == 0:
        return a
    i = a
    while i >= 1:
        if b % i == 0 and a % i == 0:
            return i
        i -= 1


def generation():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = '{} {}'.format(number1, number2)
    answer = str(gcd_check(number1, number2))
    return question, answer
