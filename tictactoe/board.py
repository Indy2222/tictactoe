class Board:

    def __init__(self):
        self._min_x = -5
        self._min_y = -5
        self._height = 11
        self._width = 11

        num_positions = self._width * self._height
        self._positions = [0] * num_positions

    def set_position(self, x: int, y: int, player: int):
        # TODO
        # 1) am I outside of the board?
        # 2) calculate new mins and width/height
        # 3) call _reinit_positions()
        # 4) assign to the board

    def _reinit_positions(self, min_x: int, min_y: int, width: int, height: int):
        # TODO better names
        old_max_x = (self._min_x + self._width)
        new_max_x = (min_x + width)
        old_max_y = (self._min_y + self._height)
        new_max_y = (min_y + height)

        shrink_left = min_x > self._min_x
        shrink_up = min_y > self._min_y
        shrink_right = old_max_x < new_max_x
        shrink_bottom = old_max_y < new_max_y

        if shrink_left or shrink_up or shrink_right or shrink_bottom:
            raise Exception('Cannot shrink the board')

        positions = [0] * (width * height)

        for dy in range(self._height):
            new_offset_y = (min_y - self._min_y) + dy
            new_index = new_offset_y * width + (min_x - self._min_x)
            old_index = dy * self._width
            positions[new_index:new_index + self._width] = self._positions[old_index:old_index + self._width]

        self._positions = positions

    def get_range(self, x: int, y: int, width: int, height: int):
        result = []
        for dy in range(height):
            row = []
            for dx in range(width):
                row.append(self.get_position(x + dx, y + dy))
            result.append(row)
        return result

    def get_position(self, x: int, y: int) -> int:
        x_offset, y_offset = self._to_offsets(x, y)

        if x_offset < 0:
            return 0
        if x_offset >= self._width:
            return 0

        if y_offset < 0:
            return 0
        if y_offset >= self._height:
            return 0

        index = y_offset * self._width + x_offset
        return self._positions[index]

    def _to_offsets(self, x: int, y: int):
        return (x - self._min_x, y - self._min_y)
