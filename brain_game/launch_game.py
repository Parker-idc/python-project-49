
import prompt


def launch(get_game_process, TITLE):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}')
    print(TITLE)
    for i in range(3):
        question, answer = get_game_process()
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
