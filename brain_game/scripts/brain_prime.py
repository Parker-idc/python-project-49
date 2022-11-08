
from brain_game.launch_game import launch
from brain_game.games.prime import get_game_process, TITLE


def main():
    launch(get_game_process, TITLE)


if __name__ == '__main__':
    main()
