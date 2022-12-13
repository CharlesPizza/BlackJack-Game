import random
class Deck():
    def __init__(self):
        self.name = "Deck 1"
        self.cards = []
        self.suits = {0:"Hearts", 1:"Spades", 2:"Diamonds", 3:"Clubs"}
    def shuffle(self):
        for suit in self.suits:
            for i in range(1, 14):
                self.cards.append(Card(i, suit))
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop()


class Card():
    def __init__(self, num, suit):
        self.value = num
        self.suit = suit

    