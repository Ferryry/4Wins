import numpy as np

class Board:

    board = []

    def create_board(self) -> np.ndarray:
        self.board = np.zeros(6, 7)
        return self.board

    def __init__(self):
        pass
