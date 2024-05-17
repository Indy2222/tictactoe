import shutil
from tictactoe.player import Player

_PLAYER_1_CHAR = 'x'
_PLAYER_2_CHAR = 'o'


def screen_size() -> tuple[int, int]:
    """Returns number of positions to be printed to the screen (widht, height).
    """
    cols, rows = shutil.get_terminal_size(fallback=(10, 10))
    return (cols - 1) // 4, (rows - 1) // 2


def print_board(board: list[list[None | Player]]):
    _clear_screen()

    for row in board:
        _print_row(row)

    if board:  # do not crash on empty board
        _print_hl(len(board[0]), end='')


def _print_row(row: list[None | Player]):
    _print_hl(len(row))

    for player in row:
        print('|', end='')
        if player == Player.PLAYER_1:
            print(' ' + _PLAYER_1_CHAR + ' ', end='')
        elif player == Player.PLAYER_2:
            print(' ' + _PLAYER_2_CHAR + ' ', end='')
        else:
            print('   ', end='')

    print('|')


def _print_hl(width: int, end='\n'):
    for _ in range(width):
        print('+---', end='')
    print('+', end=end, flush=True)


def _clear_screen():
    # Clear the screen
    print("\033[2J", end='')
    # \033[H - moves cursor to the top-left corner
    print("\033[H", end='')
