from enum import Enum


class OutOfBounds(ValueError):
    pass


class Player(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2


class Board:

    def __init__(self):
        self._min_x = -5
        self._min_y = -5
        self._height = 11
        self._width = 11

        num_positions = self._width * self._height
        self._positions = [None] * num_positions

    def set_position(self, x: int, y: int, player: Player):
        offset_x, offset_y = self._to_offsets(x, y)

        out_mins = offset_x < 0 or offset_y < 0
        out_maxs = offset_x >= self._width or offset_y >= self._height
        if out_mins or out_maxs:
            min_x = min(self._min_x, x - 10)
            min_y = min(self._min_y, y - 10)
            # TODO better names
            max_x = max(self._min_x + self._width, x + 10)
            max_y = max(self._min_y + self._height, y + 10)
            width = max_x - min_x
            height = max_y - min_y
            self._reinit_positions(min_x, min_y, width, height)

        index = self._to_index(x, y)
        self._positions[index] = player.value

    def _reinit_positions(
        self,
        min_x: int,
        min_y: int,
        width: int,
        height: int
    ):
        # TODO better names
        old_max_x = (self._min_x + self._width)
        new_max_x = (min_x + width)
        old_max_y = (self._min_y + self._height)
        new_max_y = (min_y + height)

        shrink_left = min_x > self._min_x
        shrink_up = min_y > self._min_y
        shrink_right = old_max_x > new_max_x
        shrink_bottom = old_max_y > new_max_y

        if shrink_left or shrink_up or shrink_right or shrink_bottom:
            raise Exception('Cannot shrink the board')

        positions = [None] * (width * height)

        for dy in range(self._height):
            new_offset_y = (self._min_y - min_y) + dy
            new_index = new_offset_y * width + (self._min_x - min_x)
            old_index = dy * self._width
            positions[new_index:new_index + self._width] = self._positions[old_index:old_index + self._width]

        self._min_x = min_x
        self._min_y = min_y
        self._width = width
        self._height = height
        self._positions = positions

    def get_range(self, x: int, y: int, width: int, height: int):
        result = []
        for dy in range(height):
            row = []
            for dx in range(width):
                row.append(self.get_position(x + dx, y + dy))
            result.append(row)
        return result

    def get_position(self, x: int, y: int) -> None | Player:
        try:
            index = self._to_index(x, y)
        except OutOfBounds:
            return None

        value = self._positions[index]
        if value is None:
            return None

        return Player(value)

    def _to_index(self, x: int, y: int) -> int:
        x_offset, y_offset = self._to_offsets(x, y)

        if x_offset < 0:
            raise OutOfBounds()
        if x_offset >= self._width:
            raise OutOfBounds()

        if y_offset < 0:
            raise OutOfBounds()
        if y_offset >= self._height:
            raise OutOfBounds()

        return y_offset * self._width + x_offset

    def _to_offsets(self, x: int, y: int):
        return (x - self._min_x, y - self._min_y)
