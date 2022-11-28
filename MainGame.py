from Player import Player
from Board import Board


class MainGame:

    def get_username(self, idx) -> str:
        return str(self.player[idx].get_name())

    def turn(self, player: Player):
        pass

    def round(self):
        pass

    def prepare_game(self) -> None:
        self.player[0].set_name(input("Player 1: Enter your Name: "))
        self.player[1].set_name(input("Player 2: Enter your Name: "))

        self.player[0].set_symbol(input(f"{self.player[0].get_name()}: set your symbol: "))
        self.player[1].set_symbol(input(f"{self.player[1].get_name()}: set your symbol: "))

        self.board.create()
        self.board.show()

    def __init__(self):
        self.player = [Player(), Player()]
        self.board = Board()
