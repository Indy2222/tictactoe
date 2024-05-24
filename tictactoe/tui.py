import curses
from enum import Enum
from tictactoe.player import Player

_PLAYER_1_CHAR = 'x'
_PLAYER_2_CHAR = 'o'


class Interaction(Enum):
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    PLAY = 5


def setup(func, *args, **kwargs):
    def wrapper(window, *args, **kwargs):
        curses.curs_set(0)
        func(Tui(window), *args, **kwargs)

    curses.wrapper(wrapper, *args, **kwargs)


class Tui:

    def __init__(self, window: curses.window):
        self._window = window

    def read(self) -> Interaction | None:
        code = self._window.getch()

        if code == curses.KEY_UP:
            return Interaction.MOVE_UP
        if code == curses.KEY_DOWN:
            return Interaction.MOVE_DOWN
        if code == curses.KEY_LEFT:
            return Interaction.MOVE_LEFT
        if code == curses.KEY_RIGHT:
            return Interaction.MOVE_RIGHT

        # letter 'p'
        if code == 112:
            return Interaction.PLAY

        return None

    def size(self) -> tuple[int, int]:
        """Returns number of positions to be printed to the screen (width,
        height).
        """
        rows, cols = self._window.getmaxyx()
        return (cols - 1) // 4, (rows - 1) // 2

    def print(self, board: list[list[None | Player]]):
        self._window.clear()

        # keep the screen clear if the board is empty
        if not board or not board[0]:
            return

        max_width, max_height = self.size()
        if len(board) > max_height or len(board[0]) > max_width:
            raise Exception('Cannot print the board, it is too large!')

        for i, row in enumerate(board):
            self._print_row(i, row)

        self._print_hl(len(board) * 2, len(board[0]))

        self._window.refresh()


    def _print_row(self, index: int, row: list[None | Player]):
        self._print_hl(index * 2, len(row))

        y = index * 2 + 1
        for i, player in enumerate(row):
            x = i * 4

            self._window.addstr(y, x, '|')

            if player == Player.PLAYER_1:
                self._window.addstr(y, x + 2, _PLAYER_1_CHAR)
            elif player == Player.PLAYER_2:
                self._window.addstr(y, x + 2, _PLAYER_2_CHAR)

        self._window.addstr(y, len(row) * 4, '|')


    def _print_hl(self, y: int, width: int):
        for i in range(width):
            self._window.addstr(y, i * 4, '+---')
        self._window.addstr(y, width * 4, '+')
