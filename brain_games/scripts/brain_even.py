from brain_games.cli import run
from .brain_games import greeting
import random


def is_even(x):
    return  'yes' if x % 2 == 0 else 'no'


def even():
    di = {1: random.randint(1, 10), 2: random.randint(1, 100), 3: random.randint(1, 1000)}
    count = 0
    i = 1
    while i <= 3:
        print("""Question: {}
Your answer: """.format(di.get(i)), end='')
        answer = input()
        if answer == is_even(di.get(i)):
             count +=1
             print('Correct!')
        else:
             print("""'yes' is wrong answer :(.Correct answer was 'no'.
Let's try again, Bill!""")
             break
        i += 1
    if count == 3:
        print('Congratulations, Bill!', end='')
        print('')


def main():
    greeting()
    run()
    even()


if __name__ == '__main__':
     main()
