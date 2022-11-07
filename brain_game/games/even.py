
from random import randint
from brain_game.launch_game import launch


title = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_logic():
    question = randint(1, 100)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def run_game():
    launch(game_logic, title)