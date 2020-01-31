import prompt


def welcome_user(module):
    print('Welcome to the Brain Games!')
    print(module.WELCOME)
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('')
    return name
