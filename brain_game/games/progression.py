
import random


TITLE = 'What number is missing in the progression?'


def get_progression():
    step = random.randint(1, 5)
    first_num = random.randint(1, 100)
    result = []
    length_progression = 0
    while length_progression <= 10:
        first_num += step
        result.append(first_num)
        length_progression += 1
    return result


def get_game_process():
    progression = get_progression()
    miss_num = random.randint(1, len(progression) - 1)
    answer = progression.pop(miss_num)
    progression.insert(miss_num, '..')
    question = ' '.join(map(str, progression))
    return question, str(answer)
