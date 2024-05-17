import time
from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe.tui import Tui, Interaction


def main():
    board = Board()
    tui = Tui()

    while True:
        interaction = tui.read()
        if interaction is None:
            continue

        # TODO handle the input
        # TODO: process the input

        print_output(tui, board)

        # TODO: detect game end


def print_output(tui: Tui, board: Board):
    width, height = tui.size()
    tui.print(board.get_range(0, 0, width, height))


if __name__ == '__main__':
    main()
