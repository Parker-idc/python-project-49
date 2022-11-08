
from random import randint


TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_game_process():
    question = randint(1, 100)
    answer = is_even(question)
    if answer is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
