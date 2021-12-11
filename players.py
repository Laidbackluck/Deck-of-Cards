from decks import Deck


class Player(Deck):
    def __init__(self, name):
        self.name = name
        self.hand = []

    # def draw(self, ):
    #     self.hand.append(drawCard())
    #     return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discardCard(self):
        return self.hand.pop()
