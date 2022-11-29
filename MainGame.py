from Player import Player
from Board import Board
from StatusValidator import StatusValidator


class MainGame:

    def get_username(self, idx) -> str:
        return str(self.player[idx].get_name())

    def turn(self):
        return_value = False

        print(f"Round: {self.rounds} | You both have left {self.player[0].coins} coins!")

        self.board.show()
        while not return_value:
            return_value = self.board.insert_coin(
                (int(input("{0} in which slot would you like to insert the coin (1-7): "
                           .format(self.get_username(0)))) - 1), self.player[0])
            if not return_value:
                print("Either the slot is full or you have specific a slot, which is bigger than 7 or smaller than 1.")

        return_value = False

        self.board.show()
        while not return_value:
            return_value = self.board.insert_coin(
                (int(input("{0} in which slot would you like to insert the coin (1-7): "
                           .format(self.get_username(1)))) - 1), self.player[1])

            if not return_value:
                print("Either the slot is full or you have specific a slot, which is bigger than 7 or smaller than 1.")

        self.rounds += 1

    def prepare_game(self) -> None:
        self.player[0].set_name(input("Player 1: Enter your Name: "))
        self.player[1].set_name(input("Player 2: Enter your Name: "))

        self.player[0].set_symbol(input(f"{self.player[0].get_name()}: set your symbol: "))
        self.player[1].set_symbol(input(f"{self.player[1].get_name()}: set your symbol: "))

        self.board.create()

        while not self.validator.is_winning(self.board, self.player):
            self.turn()

    def __init__(self):
        self.validator = StatusValidator()
        self.player = [Player(), Player()]
        self.board = Board()
        self.rounds = 1
