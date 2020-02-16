import random  # Used for shuffling the Deck Randomly

class Deck:
    _listCard = []
    _listPool = []

    def __init__(self):
        self.setDeck()
    
    @property
    def Cards(self):
        return self._listCard

    def setDeck(self):
        for suit in ("Diamonds", "Spades", "Hearts", "Clubs"):
            for value in range(1, 14):
                card = Card(suit, value)
                self._listCard.append(card)
    
    def listLength(self, listType = 'deck'):
        if listType == 'deck':
            return len(self._listCard)
        elif listType == 'pool':
            return len(self._listPool)
    
    def shuffle(self):
        random.shuffle(self._listCard)

    def getCard(self):
        return self._listCard.pop()

class Card:

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def __str__(self):
        return f'|{self._value} {self._suit}|'
    
    @property
    def cardValue(self):
        return self._value
    
    @property
    def cardSuit(self):
        return self._suit