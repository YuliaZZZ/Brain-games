from random import randint
from itertools import islice, count


WELCOME = 'What number is missing in the progression?'


PROGRESSION_SIZE = 10


def generation():
    number = randint(0, 9)
    progression = list(islice(count(
                start=randint(10, 50),
                step=randint(1, 10)),
                PROGRESSION_SIZE))
    secret_elem = progression[number]
    progression[number] = '..'
    a, a1, a2, a3, a4, a5, a6, a7, a8, a9 = progression
    question = (
            '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.
            format(a, a1, a2, a3, a4, a5, a6, a7, a8, a9))
    answer = str(secret_elem)
    return question, answer
