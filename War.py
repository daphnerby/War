#!/usr/bin/python3
#  need to shuffle the deck
from random import shuffle

#  explain the rules
#  THIS IS WAR.

#  variables
#  a deck is composed of the faces: 2-10, Jack, Queen, King, Ace, each with a heart, diamond, spade, club SUIT
#  make an initial dictionary of the numerical faces in a deck. in the dictionary, put [2:2, 3:3, 4:4...10:10]
faces = {value: value for value in range(2, 11)}
#  insert the numerical values for Jack, Queen, King, and Ace into the faces dictionary
faces[11] = 'J'
faces[12] = 'Q'
faces[13] = 'K'
faces[14] = 'A'

#  dictionary of suits, in unicode format. S is spade, H is heart, D is diamond, C is clubs
suits = {'S': '\u2660', 'H': '\u2665', 'D': '\u2666', 'C': '\u2663'}

# run through the for for loop, getting the values of the faces & suits in the faces & suits dictionaries.
# concatenate the values together, append it to the deck list
deck = [f'{face}{suit}' for face in faces for suit in suits.values()]

shuffle(deck)
# shuffle and split the deck
P1Deck = deck[:26]
P2Deck = deck[26:52]
P1Pile = []
P2Pile = []
Pot = []
rounds = 0
ties = 0

#  get the numerical value of the first card in the deck, compare in second deck

while (P1Deck or P1Pile) and (P2Deck or P2Pile):
    rounds += 1
    if len(P1Deck) <= 4 and P1Pile:  # check if there's too little in the deck for a tie
        shuffle(P1Pile)
        P1Deck.extend(P1Pile)
        P1Pile = []
    if len(P2Deck) <= 4 and P2Pile:  # check if there's too little in the deck for a tie
        shuffle(P2Pile)
        P2Deck.extend(P2Pile)
        P2Pile = []

    print(f'Player 1 played {faces[int(P1Deck[0][:-1])]}{P1Deck[0][-1]}.',
          f'Player 2 played {faces[int(P2Deck[0][:-1])]}{P2Deck[0][-1]}.', end=' ')
    if int(P1Deck[0][:-1]) > int(P2Deck[0][:-1]):  # if Player 1 won this round
        print('Player 1 won this round.')
        P1Pile.append(P1Deck.pop(0))
        P1Pile.append(P2Deck.pop(0))
        P1Pile.extend(Pot)
        Pot = []
    elif int(P1Deck[0][:-1]) < int(P2Deck[0][:-1]):  # if player 2 won this round
        print('Player 2 won this round.')
        P2Pile.append(P1Deck.pop(0))
        P2Pile.append(P2Deck.pop(0))
        P2Pile.extend(Pot)  # put the contents of the pot into player 2's pile
        Pot = []  # empty the pot
    else:  # TIE TIME!!!
        ties += 1
        if int(P1Deck[0][0:-1]) == 14:  # Did a pair of Aces tie? burn 3 cards
            if len(P1Deck) <= 4 or len(P2Deck) <= 4:
                break
            print('A pair of Aces!  Time to burn 3 cards and keep playing.')
            Pot.extend([*P1Deck[:4], *P2Deck[:4]])
            del P1Deck[:4]
            del P2Deck[:4]
        else:  # Did a pair of regular cards tie? burn 1 card
            if len(P1Deck) <= 2 or len(P2Deck) <= 2:
                break
            print('A tie! Time to burn a card and keep playing.')
            Pot.extend([*P1Deck[:2], *P2Deck[:2]])
            del P1Deck[:2]
            del P2Deck[:2]

print("Player 1 won!") if len(P1Deck) + len(P1Pile) > len(P2Deck) + len(P2Pile) else print("Player 2 won")
print(f'There were {ties} ties out of {rounds} rounds; {100 * ties / rounds:.2f}% ties!')
