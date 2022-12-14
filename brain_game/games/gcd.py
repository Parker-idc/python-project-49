import random

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    min_num, max_num = min(num1, num2), max(num1, num2)
    divisor = min_num
    while divisor > 0:
        if max_num % divisor == 0 and min_num % divisor == 0:
            answer = divisor
            return answer
        divisor -= 1


def get_game_round():
    num1, num2 = random.choices(range(1, 30), k=2)
    answer = get_gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, str(answer)
