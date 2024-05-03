from tictactoe.board import Board, Player


def test_board():
    board = Board()

    board.set_position(0, 0, Player.PLAYER_2)
    board.set_position(-1, -1, Player.PLAYER_1)
    board.set_position(-100, 20, Player.PLAYER_2)
    board.set_position(1, 0, Player.PLAYER_1)

    result = board.get_range(0, -1, 4, 5)
    expected_result = [
        [None, None, None, None],
        [Player.PLAYER_2, Player.PLAYER_1, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]
    assert result == expected_result

    result = board.get_range(-101, 20, 2, 3)
    expected_result = [
        [None, Player.PLAYER_2],
        [None, None],
        [None, None],
    ]
    assert result == expected_result

    result = board.get_range(10000, 20000, 4, 2)
    expected_result = [
        [None, None, None, None],
        [None, None, None, None],
    ]
    assert result == expected_result
