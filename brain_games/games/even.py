from random import randint


welcome = 'Answer "yes" if number even otherwise answer "no".'


def func():
    def even_check(x):
        return 'yes' if x % 2 == 0 else 'no'
    question = randint(1, 1000)
    return question, even_check(question)
