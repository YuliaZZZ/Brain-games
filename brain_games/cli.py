import prompt


def welcome_user(welcome):
    print('Welcome to the Brain Games!')
    print(welcome)
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('')
    return name
