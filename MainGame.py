from Player import Player


class MainGame:
    player = [Player()] * 2

    def get_username(self, idx) -> str:
        return str(self.player[idx].get_name())

    def prepare_game(self) -> None:
        self.player[0].set_name(input("Player 1: Enter your Name: "))
        self.player[1].set_name(input("PLayer 2: Enter your Name: "))
        print("{} is playing against {}".format(self.player[0].get_name(), self.player[0].get_name()))

        self.player[0].set_symbol(input(f"{self.player[0].get_symbol()!s}: set your symbol: "))
        self.player[1].set_symbol(input(f"{self.player[1].get_symbol()!s}: set your symbol: "))
        print("{} is using {}".format(self.player[0].get_name(), self.player[0].get_symbol()))
        print("{} is using {}".format(self.player[1].get_name(), self.player[1].get_symbol()))

    def __init__(self):
        pass
