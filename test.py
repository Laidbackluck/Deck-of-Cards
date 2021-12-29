import csv
from random import shuffle

cards_csv = "Deck_data/cards.csv"


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


class Deck:
    def __init__(self):
        self.__cards = []

    def __repr__(self):
        return f"{self.cards}"

    @classmethod
    def create_deck(cls):
        with open(cards_csv, "r") as f:
            reader = csv.DictReader(f)
            deck = list(reader)

        inst = cls()

        for card in deck:
            card = Card(
                suit=str(card.get("suit")),
                rank=str(card.get("rank"))
            )
            inst.cards.append(card.name)

        return inst

    @property
    def cards(self):
        return self.__cards

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()

deck1 = Deck.create_deck()
deck1.shuffle()
print(deck1.drawCard)


