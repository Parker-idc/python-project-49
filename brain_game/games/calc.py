
import random
from brain_game.launch_game import launch


title = 'What is the result of the expression?'


def task():
    num1, num2 = random.choices(range(1, 20), k=2)
    signs = random.choice(['+', '-', '*'])
    return num1, signs, num2


def game_logic():
    num1, signs, num2 = task()
    if signs == '+':
        answer = num1 + num2
    if signs == '-':
        answer = num1 - num2
    if signs == '*':
        answer = num1 * num2
    question = "{} {} {}".format(num1, signs, num2)
    return question, answer


def run_game():
    launch(game_logic, title)
