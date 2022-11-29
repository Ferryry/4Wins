from Player import Player
from Board import Board


class StatusValidator:

    def validate_vertical(self) -> bool:
        pass

    def validate_horizontal(self) -> bool:
        pass

    def validate_diagonally(self) -> bool:
        pass

    def validate(self) -> bool:
        if (self.player[0].coins or self.player[1].coins) == 0:
            return True

        if self.validate_horizontal() or self.validate_vertical() or self.validate_diagonally():
            return True

        return False



    def is_winning(self, board: Board, player: list[Player]) -> bool:
        self.player = player
        self.board = board
        return self.validate()



    def __init__(self):
        self.winner = None
        self.player = None
        self.board = None
