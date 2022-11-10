
from random import randint


TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game_round():
    question = randint(1, 100)
    answer = is_even(question)
    if answer is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
