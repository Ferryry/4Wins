import Player


class Board:
    board = []

    def get_board(self) -> list:
        return self.board

    def return_last_empty_slot(self, offset: int) -> int:
        if -1 < offset < 7:
            for index, item in reversed(list(enumerate(self.board))):
                if str(item[offset]) == "_":
                    return index

            return -1
        return -1

    def insert_coin(self, column_offset: int, player: Player) -> bool:
        offset = self.return_last_empty_slot(column_offset)
        if offset > -1:
            self.board[offset][column_offset] = player.get_symbol()
            player.coins -= 1
            return True
        return False

    def create(self) -> None:
        self.board = [["_" for col in range(7)] for row in range(6)]

    def show(self):
        for b in self.board:
            for sub in b:
                print(f" {sub} ", end="")

            print("\n", end="")

        print(" -------------------\n 1  2  3  4  5  6  7 ")

    def __init__(self):
        self.board = None
