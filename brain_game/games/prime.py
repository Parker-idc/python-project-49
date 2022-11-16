import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    index = 2
    while index <= num // 2:
        if num % index == 0:
            return False
        index += 1
    return True


def get_game_round():
    question = random.randint(2, 30)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
