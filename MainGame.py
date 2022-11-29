from Player import Player
from Board import Board
from StatusValidator import StatusValidator


class MainGame:

    def get_username(self, idx) -> str:
        return str(self.player[idx].get_name())

    def insert_coin(self, column_offset: int, player: Player) -> None:
        self.board.board.insert(column_offset, player.get_symbol())

    def turn(self):

        print(f"Round: {self.rounds}")

        self.board.show()
        self.insert_coin((int(input("{0} in which slot would you like to insert the coin (1-7): "
                                    .format(self.player[0].get_name()))) - 1), self.player[0])

        self.board.show()
        self.insert_coin((int(input("{0} in which slot would you like to insert the coin (1-7): "
                                    .format(self.player[1].get_name()))) - 1), self.player[1])

    def prepare_game(self) -> None:
        self.player[0].set_name(input("Player 1: Enter your Name: "))
        self.player[1].set_name(input("Player 2: Enter your Name: "))

        self.player[0].set_symbol(input(f"{self.player[0].get_name()}: set your symbol: "))
        self.player[1].set_symbol(input(f"{self.player[1].get_name()}: set your symbol: "))

        self.board.create()

        while not StatusValidator.is_winning():
            self.turn()
            self.rounds += 1

    def __init__(self):
        self.player = [Player(), Player()]
        self.board = Board()
        self.rounds = 1
