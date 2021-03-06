import csv
from random import shuffle
from cards import Card

cards_csv = "Deck_data/cards.csv"


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

