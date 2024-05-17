import time
from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe import tui


def main():
    board = Board()

    while True:
        # TODO: read input from the user
        # TODO: process the input

        print_output(board)
        time.sleep(1)


def print_output(board: Board):
    width, height = tui.screen_size()
    tui.print_board(board.get_range(0, 0, width, height))


if __name__ == '__main__':
    main()
