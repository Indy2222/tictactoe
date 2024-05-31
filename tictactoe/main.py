from tictactoe.player import Player
from tictactoe.board import Board
from tictactoe import tui
from tictactoe.tui import Interaction, Tui, Symbol, Style


WIN_STREAK_LEN = 5


def main():
    board = Board()
    tui.setup(start_game, board=board)


class Game:

    def __init__(self, tui: Tui, board: Board):
        self._tui = tui
        self._board = board

        self._x = 0
        self._y = 0
        self._player = Player.PLAYER_1
        self._win_streak = None

    def run(self):
        self.refresh()

        should_quit = False
        while not should_quit:
            interaction = self._tui.read()
            if interaction is None:
                continue

            should_quit = self.handle_interaction(interaction)
            self.refresh()

    def handle_interaction(self, interaction: Interaction) -> bool:
        if interaction == Interaction.QUIT:
            return True

        if self._win_streak is None and interaction == Interaction.PLAY:
            self.play()
        elif interaction == Interaction.MOVE_UP:
            self._y -= 1
        elif interaction == Interaction.MOVE_DOWN:
            self._y += 1
        elif interaction == Interaction.MOVE_LEFT:
            self._x -= 1
        elif interaction == Interaction.MOVE_RIGHT:
            self._x += 1

        return False

    def play(self):
        current = self._board.get_position(self._x, self._y)
        if current is not None:
            return False

        self._board.set_position(self._x, self._y, self._player)
        self._player = self._player.invert()
        self._win_streak = self.detect_win_streak()

    def refresh(self):
        width, height = self._tui.size()
        rel_x, rel_y = width // 2, height // 2

        corner_x = self._x - rel_x
        corner_y = self._y - rel_y
        rect = self._board.get_range(corner_x, corner_y, width, height)

        extra_symbols = []

        if self._win_streak is None:
            player = self._board.get_position(self._x, self._y)
            if player is None:
                extra_symbols.append(Symbol(
                    player=self._player,
                    style=Style.ALLOWED,
                    x=rel_x,
                    y=rel_y
                ))
            else:
                extra_symbols.append(Symbol(
                    player=player,
                    style=Style.FORBIDDEN,
                    x=rel_x,
                    y=rel_y
                ))
        else:
            assert self._win_streak

            first_x, first_y = self._win_streak[0]
            player = self._board.get_position(first_x, first_y)
            assert player is not None, (first_x, first_y)

            for x, y in self._win_streak:
                extra_symbols.append(Symbol(
                    player=player,
                    style=Style.HIGHLIGHTED,
                    x=x - corner_x,
                    y=y - corner_y,
                ))

        self._tui.display(rect, extra_symbols)

    def detect_win_streak(self) -> list[tuple[int, int]] | None:
        """Returns True if the given positoin is part of a winning streak."""
        player = self._board.get_position(self._x, self._y)
        if player is None:
            return None

        directions = [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1)
        ]

        for direction in directions:
            win_streak = self.test_streak_dir(player, direction)
            if win_streak:
                return win_streak

        return None

    def test_streak_dir(
        self,
        player: Player,
        direction: tuple[int, int],
    ) -> list[tuple[int, int]] | None:
        pos_x, pos_y = self._x, self._y
        dir_x, dir_y = direction

        while True:
            next_pos_x, next_pos_y = pos_x + dir_x, pos_y + dir_y
            pos_player = self._board.get_position(next_pos_x, next_pos_y)
            if pos_player != player:
                break
            pos_x, pos_y = next_pos_x, next_pos_y

        dir_x *= -1
        dir_y *= -1

        streak = [(pos_x, pos_y)]
        while True:
            pos_x += dir_x
            pos_y += dir_y
            pos_player = self._board.get_position(pos_x, pos_y)
            if pos_player != player:
                break
            streak.append((pos_x, pos_y))

        if len(streak) >= WIN_STREAK_LEN:
            return streak

        return None


def start_game(tui: Tui, board: Board):
    game = Game(tui, board)
    game.run()
