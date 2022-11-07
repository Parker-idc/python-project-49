
import random
from brain_game.launch_game import launch


title = 'Find the greatest common divisor of given numbers.'


def task():
    num1, num2 = random.choices(range(1, 20), k=2)
    return num1, num2


def game_logic():
    num1, num2 = task()
    min_num, max_num = min(num1, num2), max(num1, num2)
    divisor = min_num
    while divisor > 0:
        if max_num % divisor == 0 and min_num % divisor == 0:
            question = "{} {}".format(num1, num2)
            answer = divisor
            return question, answer
        divisor -= 1


def run_game():
    launch(game_logic, title)
