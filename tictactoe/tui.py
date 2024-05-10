from tictactoe.player import Player

CROSS = '❌'
CIRCLE = '⬤'
SQUARE = '□'

def print_board(board: list[list[None | Player]]):
    clear_screen()
    print('test')


def clear_screen():
    # Clear the screen
    print("\033[2J", end='')
    # \033[H - moves cursor to the top-left corner
    print("\033[H", end='')
