from enum import Enum
from curses import cbreak, initscr, KEY_UP, KEY_LEFT, KEY_DOWN, KEY_RIGHT, KEY_ENTER
import shutil
from tictactoe.player import Player

_PLAYER_1_CHAR = 'x'
_PLAYER_2_CHAR = 'o'


class Interaction(Enum):
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    PLAY = 5


class Tui:

    def __init__(self):
        self._window = initscr()
        cbreak()
        self._window.keypad(True)
        # TODO might be unnecessary
        self._window.nodelay(False)

    def read(self) -> Interaction | None:
        code = self._window.getch()

        if code == KEY_UP:
            return Interaction.MOVE_UP
        if code == KEY_DOWN:
            return Interaction.MOVE_DOWN
        if code == KEY_LEFT:
            return Interaction.MOVE_LEFT
        if code == KEY_RIGHT:
            return Interaction.MOVE_RIGHT
        if code == KEY_ENTER:
            return Interaction.PLAY

        return None

    def size(self) -> tuple[int, int]:
        """Returns number of positions to be printed to the screen (widht,
        height).
        """
        cols, rows = shutil.get_terminal_size(fallback=(10, 10))
        return (cols - 1) // 4, (rows - 1) // 2


    def print(self, board: list[list[None | Player]]):
        self._window.erase()

        for row in board:
            self._print_row(row)

        if board:  # do not crash on empty board
            self._print_hl(len(board[0]), end='')

        self._window.refresh()


    def _print_row(self, row: list[None | Player]):
        self._print_hl(len(row))

        for player in row:
            # TOOD
            # self._window.move()

            print('|', end='')
            if player == Player.PLAYER_1:
                print(' ' + _PLAYER_1_CHAR + ' ', end='')
            elif player == Player.PLAYER_2:
                print(' ' + _PLAYER_2_CHAR + ' ', end='')
            else:
                print('   ', end='')

        print('|', end='')


    def _print_hl(self, width: int, end='\n'):
        for _ in range(width):
            print('+---', end='')
        print('+', end='', flush=True)


