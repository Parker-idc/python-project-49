import random


GAME_RULE = 'What is the result of the expression?'


def get_calc_operation(num1, num2, sign):
    if sign == '+':
        answer = num1 + num2
    if sign == '-':
        answer = num1 - num2
    if sign == '*':
        answer = num1 * num2
    return answer


def get_game_round():
    sign = random.choice(['+', '-', '*'])
    num1, num2 = random.choices(range(1, 20), k=2)
    answer = get_calc_operation(num1, num2, sign)
    question = f"{num1} {sign} {num2}"
    return question, str(answer)
