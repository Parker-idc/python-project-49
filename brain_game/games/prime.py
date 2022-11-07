import random
from brain_game.launch_game import launch


title = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    question = random.randint(1, 30)
    divider = 0
    for i in range(1, question + 1):
        if question % i == 0:
            divider += 1

    if divider == 2:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def run_game():
    launch(game_logic, title)
