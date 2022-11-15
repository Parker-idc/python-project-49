import random

GAME_RULE = 'What number is missing in the progression?'


def get_progression(start_num, step, length_progression):
    progression = []
    start_length_progression = 0
    while start_length_progression <= length_progression:
        start_num += step
        progression.append(start_num)
        start_length_progression += 1
    return progression


def get_game_round():
    length_progression = 10
    step = random.randint(1, 5)
    start_num = random.randint(1, 100)
    progression = get_progression(start_num, step, length_progression)
    miss_num = random.randint(1, len(progression) - 1)
    answer = progression.pop(miss_num)
    progression.insert(miss_num, '..')
    question = ' '.join(map(str, progression))
    return question, str(answer)
