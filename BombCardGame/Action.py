def showHand(player):
    for card in player.Hand:
        print(str(card), end = "")

def dealtCard(player, deck, num):
    for i in range(num):
        player.setCard(deck.getCard())

def played(player, card):
    return player.getCard(card)

