from enum import Enum


class Player(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2

    def invert(self):
        if self == Player.PLAYER_1:
            return Player.PLAYER_2
        else:
            return Player.PLAYER_1
