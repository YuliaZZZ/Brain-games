from brain_games.cli import welcome_user
import prompt


def engine(module):
    name = welcome_user(module.welcome)
    i = 1
    while i <= 3:
        question, chek_question = module.func()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == chek_question:
            print('Correct!')
        else:
            print("""'{}' is wrong answer :(.Correct answer was '{}'.
Let's try again, {}!""".format(answer, chek_question, name))
            break
        i += 1
    else:
        print('Congratulations, {}!'.format(name))
