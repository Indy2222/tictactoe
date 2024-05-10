from tictactoe.player import Player
from tictactoe.tui import print_board


def main():
    print_board([
        [None, None, Player.PLAYER_1],
        [None, None, Player.PLAYER_1],
        [Player.PLAYER_2, None, Player.PLAYER_2]
    ])


if __name__ == '__main__':
    main()
