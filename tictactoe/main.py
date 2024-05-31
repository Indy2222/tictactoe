from tictactoe.player import Player
from tictactoe.board import Board
from tictactoe import tui
from tictactoe.tui import Interaction, Tui


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

        if interaction == Interaction.MOVE_UP:
            self._y -= 1
        elif interaction == Interaction.MOVE_DOWN:
            self._y += 1
        elif interaction == Interaction.MOVE_LEFT:
            self._x -= 1
        elif interaction == Interaction.MOVE_RIGHT:
            self._x += 1
        elif interaction == Interaction.PLAY:
            self.play()

        return False

    def play(self):
        current = self._board.get_position(self._x, self._y)
        if current is not None:
            return

        self._board.set_position(self._x, self._y, self._player)
        self._player = self._player.invert()

    def refresh(self):
        width, height = self._tui.size()
        x = self._x - width // 2
        y = self._y - height // 2
        rect = self._board.get_range(x, y, width, height)

        player = self._board.get_position(self._x, self._y)
        allowed = False

        if player is None:
            player = self._player
            allowed = True

        player_pos = (width // 2, height // 2)

        self._tui.display(rect, player, player_pos, allowed)


def start_game(tui: Tui, board: Board):
    game = Game(tui, board)
    game.run()
