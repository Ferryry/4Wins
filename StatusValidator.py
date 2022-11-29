from Player import Player
from Board import Board


class StatusValidator:

    def validate_vertically(self) -> bool:
        pass

    def validate_horizontally(self) -> bool:
        for player in self.players:
            for row in self.board.get_board():
                matches = 0
                for index, column in enumerate(row):
                    if matches == 4:
                        return True

                    if index == 6:
                        break

                    if column == player.get_symbol():
                        matches += 1
                    else:
                        matches = 0

        return False


    def validate_diagonally(self) -> bool:
        pass

    def validate(self) -> bool:
        if (self.players[0].coins or self.player[1].coins) == 0:
            return True

        #if self.validate_horizontal() or self.validate_vertical() or self.validate_diagonally():
        #    return True

        if self.validate_horizontally():
            return True

        return False

    def is_winning(self, board: Board, players: list[Player]) -> bool:
        self.players = players
        self.board = board
        return self.validate()

    def __init__(self):
        self.winner = None
        self.players = None
        self.board = None
