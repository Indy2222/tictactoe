from tictactoe.board import Board


def test_board():
    board = Board()

    board.set_position(0, 0, 2)
    board.set_position(-1, -1, 1)
    board.set_position(-100, 20, 2)
    board.set_position(1, 0, 1)

    result = board.get_range(0, -1, 4, 5)
    expected_result = [
        [0, 0, 0, 0],
        [2, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    assert result == expected_result

    result = board.get_range(-101, 20, 2, 3)
    expected_result = [
        [0, 2],
        [0, 0],
        [0, 0],
    ]
    assert result == expected_result

    result = board.get_range(10000, 20000, 4, 2)
    expected_result = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    assert result == expected_result
