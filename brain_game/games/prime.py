
import random


TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divider = 0
    index = 1
    while index <= num // 2:
        if num % index == 0:
            divider += 1
        index += 1
    return divider == 1


def get_game_round():
    question = random.randint(1, 30)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
