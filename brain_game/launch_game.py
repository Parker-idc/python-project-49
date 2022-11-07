
import prompt


def launch(game_logic, title):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}')
    print(title)
    for i in range(3):
        question, answer = game_logic()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if str(user_answer) == str(answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
