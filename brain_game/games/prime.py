
import random


TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divider = 0
    for i in range(1, (num + 2) // 2):
        if num % i == 0:
            divider += 1
    if divider == 1:
        return True
    else:
        return False


def get_game_process():
    question = random.randint(1, 30)
    divider = is_prime(question)
    if divider is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
