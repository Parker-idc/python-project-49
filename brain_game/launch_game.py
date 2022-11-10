
import prompt


TRIES_COUNT = 3


def launch_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}')
    print(game.TITLE)
    for i in range(TRIES_COUNT):
        question, answer = game.get_game_round()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
