
import random


TITLE = 'What is the result of the expression?'


def calc_operation(num1, num2, signs):
    if signs == '+':
        answer = num1 + num2
    if signs == '-':
        answer = num1 - num2
    if signs == '*':
        answer = num1 * num2
    return answer


def get_game_round():
    sign = random.choice(['+', '-', '*'])
    num1, num2 = random.choices(range(1, 20), k=2)
    answer = calc_operation(num1, num2, sign)
    question = "{} {} {}".format(num1, sign, num2)
    return question, str(answer)
