from Deck import deck
from Player import player
import time

def main():
    list_Deck = deck()
    list_Comps_Name = ["Noob1", "Noob2", "Noob3", "Noob4"]
    list_Players = []

    # START GAME
    game_Flag = True
    game_input = input("Valdaz Digital Bomb | Press Enter to Cont... / Q to Quit! ")

    if game_input.lower() == 'q':
        game_Flag = False 

    name = input("Enter Player Name: ")
    noob = player(name)

    while game_Flag:
        numPlayers = int(input("Number of Players: "))

        print("Lets Play!!!")

        list_Deck.shuffle()

        print("Shuffling. . ."); time.sleep(2)

        for i in range(numPlayers):
            temp = player(list_Comps_Name[i])
            list_Comps.append(temp)

        for temp in list_Comps:
            print(temp.hand)
        
        game_Flag = False

    # END GAME

if __name__ == "__main__":
    main()