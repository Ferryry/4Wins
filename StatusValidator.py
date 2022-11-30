from Player import Player
from Board import Board


class StatusValidator:

    def validate_vertically(self) -> bool:
        for player in self.players:
            for vertical_index in range(0, 5):

                matches = 0

                for horizontal_index in range(0, 6):
                    if self.board.get_board()[horizontal_index][vertical_index] == player.get_symbol():
                        matches += 1
                    else:
                        matches = 0

                    if matches == 4:
                        self.winner = player
                        return True

    def validate_horizontally(self) -> bool:
        for player in self.players:
            for row in self.board.get_board():

                matches = 0

                for index, column in enumerate(row):
                    if index == 6:
                        break

                    if column == player.get_symbol():
                        matches += 1
                    else:
                        matches = 0

                    if matches == 4:
                        self.winner = player
                        return True

        return False

    def validate_diagonally(self) -> bool:
        for player in self.players:

            decrement = 0
            matches = 0

            for index, item in enumerate(self.board.get_board()):
                if matches == 4:
                    self.winner = player
                    return True

                if self.board.get_board()[5 - decrement][index] == player.get_symbol():
                    matches += 1

                decrement += 1

            decrement = 0
            matches = 0

            for index, item in enumerate(self.board.get_board()):
                if matches == 4:
                    self.winner = player
                    return True

                if self.board.get_board()[decrement][index] == player.get_symbol():
                    matches += 1

                decrement += 1

    def validate(self) -> bool:
        if (self.players[0].coins or self.players[1].coins) == 0:
            return True

        if self.validate_horizontally() or self.validate_vertically() or self.validate_diagonally():
            return True

        return False

    def is_winning(self, board: Board, players: list[Player]) -> None:
        self.players = players
        self.board = board
        self.gameover = True if self.validate() else False

    def __init__(self):
        self.winner = None
        self.players = None
        self.board = None
        self.gameover = False
