import os

from Player import Player
from Board import Board
from StatusValidator import StatusValidator


class MainGame:

    def get_username(self, index) -> str:
        return str(self.player[index].get_name())

    def turn(self) -> None:
        return_value = False

        print(f"Round: {self.rounds} | You both have left {self.player[0].coins} coins!")
        question = "{0} in which slot would you like to insert the coin (1-7): "

        self.board.show()
        while not return_value:
            try:
                slot_input = input(question.format(self.get_username(0)))
                slot_input = int(slot_input)
                return_value = self.board.insert_coin(slot_input, self.player[0])
            except:
                print("{} is not a valid slot".format(slot_input))

            if not return_value:
                print("Either the slot is full or you have specific a slot, which is bigger than 7 or smaller than 1.")

        self.validator.is_winning(self.board, self.player)
        return_value = False

        self.board.show()
        while not return_value:
            try:
                slot_input = input(question.format(self.get_username(1)))
                slot_input = int(slot_input)
                return_value = self.board.insert_coin(slot_input, self.player[1])
            except:
                print("{} is not a valid slot".format(slot_input))

            if not return_value:
                print("Either the slot is full or you have specific a slot, which is bigger than 7 or smaller than 1.")

        self.validator.is_winning(self.board, self.player)
        self.rounds += 1

    def prepare_game(self) -> None:
        self.player[0].set_name(input("Player 1: Enter your Name: "))
        self.player[1].set_name(input("Player 2: Enter your Name: "))
        self.player[0].set_symbol("X")
        self.player[0].set_symbol("O")
        self.player[0].coins = self.player[1].coins = 21

        self.board.create()

        while not self.validator.gameover:
            self.turn()

        if self.validator.winner is not None:
            print(f"{self.validator.winner.get_name()} has won!")
        else:
            print("Game Over - Nobody has won")

        if str(input("Would you like to restart? (y/n): ")) == "y":
            self.prepare_game()

    def __init__(self):
        self.validator = StatusValidator()
        self.player = [Player(), Player()]
        self.board = Board()
        self.rounds = 1
