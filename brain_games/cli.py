import prompt


def welcome_user(WELCOME):
    print('Welcome to the Brain Games!')
    print(WELCOME)
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('')
    return name
