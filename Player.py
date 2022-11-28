class Player:

    name = ''
    symbol = ''

    def set_symbol(self, symbol) -> None:
        self.symbol = symbol

    def get_symbol(self) -> str:
        return self.symbol

    def set_name(self, name) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def __init__(self):
        pass
