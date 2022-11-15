import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    index = 2
    while index <= num // 2:
        if num % index == 0:
            return False
        index += 1


def get_game_round():
    question = random.randint(2, 30)
    answer = 'no' if is_prime(question) is False else 'yes'
    return question, answer
