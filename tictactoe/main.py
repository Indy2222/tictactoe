from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe import tui


def main():
    board = Board()
    tui.setup(game_loop, board=board)


def game_loop(tui: tui.Tui, board: Board):
    width, height = tui.size()
    tui.print(board.get_range(0, 0, width, height))

    while True:
        interaction = tui.read()
        if interaction is None:
            continue

        # TODO handle the input
        # TODO: process the input

        width, height = tui.size()
        tui.print(board.get_range(0, 0, width, height))

        # TODO: detect game end


if __name__ == '__main__':
    main()
