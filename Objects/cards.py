class Card:

    def __init__(self, suit: str, rank: str):
        self.__suit = suit
        self.__rank = rank
        self.__name = f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    @property # Read-only Attribute
    def suit(self):
        return self.__suit

    @property # Read-only Attribute
    def rank(self):
        return self.__rank

    @property # Read-only Attribute
    def name(self):
        return self.__name

    def show(self):
        print(f"{self.rank} of {self.suit}")

