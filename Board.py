from os import linesep
from typing import Optional

class Board:
    board = []

    def return_last_empty_slot(self, offset: int) -> Optional[int]:
        for idx, item in enumerate(self.board):
            if not str(item[offset]) == "0":
                return idx
        else:
            return Optional[None]

    def create(self) -> None:
        self.board = [[0 for col in range(7)] for row in range(6)]

    def show(self):
        for b in self.board:
            for sub in b:
                print(f" {sub} ", end="")

            print("\n", end="")

        print(" -------------------\n 1  2  3  4  5  6  7 ")

    def __init__(self):
        pass
