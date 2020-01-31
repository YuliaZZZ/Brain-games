from random import randint


WELCOME = 'Answer "yes" if number even otherwise answer "no".'


def even_check(x):
    return 'yes' if x % 2 == 0 else 'no'


def generation():
    question = randint(1, 1000)
    answer = even_check(question)
    return question, answer
