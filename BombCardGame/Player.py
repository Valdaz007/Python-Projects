class Player:
    _numPlayer = 0

    def __init__(self, name):
        self._name = name
        self._hand = []
        self._numPlayer += 1
    
    @property
    def Hand(self):
        return self._hand
    
    @property
    def Name(self):
        return self._name
    
    def setCard(self, card):
        self._hand.append(card)

    def getCard(self, card):
        return self._hand.pop(card)