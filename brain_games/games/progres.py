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
    for i, _ in enumerate(progression):
        if i < 9:
            progression[i] = str(progression[i]) + ', '
        progression[i] = str(progression[i])
    question = ''.join(progression)
    answer = str(secret_elem)
    return question, answer
