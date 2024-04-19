class Board:

    def __init__(self):
        self._min_x = -5
        self._min_y = -5
        self._height = 11
        self._width = 11

        num_positions = self._width * self._height
        self._positions = [0] * num_positions

    def set_position(self, x: int, y: int, player: int):
        # TODO extend board if out of range
        x_offset, y_offset = self._to_offsets(x, y)

        if x_offset < 0:
            min_x = x - 10
            x_shift = min_x - self._min_x
            width = abs(x_shift) + self._width
            positions = [0] * (width * self._height)

            for i in range(len(self._positions)):
                x = i // self._width + x_shift
                y = i - (i // self._width)
                index = y * width + x
                positions[index] = self._positions[i]

            self._positions = positions

        # TODO set the position

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
