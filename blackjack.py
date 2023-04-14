import random
import sys

cardsToValues = {
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":10,
    "Q":10,
    "K":10,
    "A":11
}



def drawCard(type): # type = "player"/"dealer"/"hidden"
    card, value = random.choice(list(cardsToValues.items()))
    if type == "player":
        if card == "A":
            print("Card drawn for player is '{a}', value: 1/{b}".format(a = card, b = value))
        else:
            print("Card drawn for player is '{a}', value: {b}.".format(a = card, b = value))
    elif type == "dealer":
        if card == "A":
            print("Card drawn for dealer is '{a}', value: 1/{b}".format(a = card, b = value))
        else: 
            print("Card drawn for dealer is '{a}', value: {b}.".format(a = card, b = value))
    elif type == "hidden":
        print("Card drawn for dealer is '???', value: ???")
    return card, value



# ace check alters the value of the ace to be 1 or 11 depending on the total of the hand.
def aceCheck(total, cardsList, card):
    if total > 11:
        cardsList.append(card)
        return 1
    else:
        cardsList.append(card)
        return 11




def playBlackjack():
    print("\nStarting a new game of Blackjack...")
    # starting new empty hands and 0 totals for player and dealer.
    playerCards = []
    playerTotal = 0
    
    dealerCards = []
    dealerTotal = 0
    
    # first drawing two cards for player
    for i in range(2):
        card, value = drawCard("player")
        if card == "A":
            playerTotal += aceCheck(playerTotal, playerCards, card)
        else:
            playerTotal += value
            playerCards.append(card)
    
    # print cards, and card total for player
    print("Player's cards are: {a}".format(a = playerCards))
    print("Player's card total is: {a}\n".format(a = playerTotal))
    
    
    # drawing two cards for dealer - one face up and one faced down
    dCard, dValue = drawCard("dealer") # first shown card for dealer
    if dCard == "A":
        dealerTotal += aceCheck(dealerTotal, dealerCards, dCard)
    else:
        dealerTotal += dValue
        dealerCards.append(dCard)
        
    displayedDealerTotal = dealerTotal
    
    dCard, dValue = drawCard("hidden") # second card hidden for dealer
    if dCard == "A":
        dealerTotal += aceCheck(dealerTotal, dealerCards, dCard)
    else:
        dealerTotal += dValue
        dealerCards.append(dCard)
        
    
    displayedDealerCards = dealerCards.copy()
    displayedDealerCards[-1] = "???"
        
    # print cards, and card total for player
    print("Dealer's cards are: {a}".format(a = displayedDealerCards))
    print("Dealer's card total is: {a}\n".format(a = displayedDealerTotal))
    
    if playerTotal == 21:
        print("Blackjack! You win!") # player hits a blackjack
    else:
        # prompt user if theyd like to hit or stand
        choice = input("Would you like to hit or stand? (H/S) ").lower()
        while choice != "s":
            newCard, newValue = drawCard("player") # drawn card displayed
            if newCard == "A":
                playerTotal += aceCheck(playerTotal, playerCards, newCard)
            else:
                playerTotal += newValue
                playerCards.append(newCard)
            print("Player's cards are: {a}".format(a = playerCards))
            print("Player's card total is: {a}\n".format(a = playerTotal))
            if playerTotal == 21:
                choice = "s"
                break
            elif playerTotal > 21:
                print("Bust! Dealer wins.") # ending where player busts
                playAgain = input("Would you like to play again? (y/n) ").lower()
                if playAgain == "y":
                    playBlackjack()
                else:
                    sys.exit()
            choice = input("Would you like to hit or stand? (H/S) ").lower()
                
        # shows hidden card for dealer and dealer true total
        print("\nDealer's cards are: {a}".format(a = dealerCards))
        print("Dealer's card total is: {a}\n".format(a = dealerTotal))
        
        if dealerTotal == 21:
            print("Blackjack! Dealer wins.")
            playAgain = input("Would you like to play again? (y/n) ").lower()
            if playAgain == "y":
                playBlackjack()
            else:
                sys.exit()
        
        else:
            # dealer hits until his total is greater or equal to 17.
            while dealerTotal < 17 and playerTotal <= 21:
                dealerNewCard, dealerNewValue = drawCard("dealer") # drawn card displayed
                if dealerNewCard == "A":
                    dealerTotal += aceCheck(dealerTotal, dealerCards, dealerNewCard)
                else:
                    dealerTotal += dealerNewValue
                    dealerCards.append(dealerNewCard)
                print("Dealer's cards are: {a}".format(a = dealerCards))
                print("Dealer's card total is: {a}\n".format(a = dealerTotal))
        
        
        # comparing totals to see outcome of game
        if playerTotal == dealerTotal:
            print("Push! You and the dealer drew!") # working on winning options
        elif dealerTotal > 21:
            print("Dealer busts! Player wins.")
                
        elif playerTotal > dealerTotal and playerTotal <= 21:
            print("Player wins!")
            
        else:
            print("Dealer wins!")
            
        playAgain = input("Would you like to play again? (y/n) ").lower()
        if playAgain == "y":
            playBlackjack()
        else:
            sys.exit()

    
    
playBlackjack()
   
    
# REPORT
"""
1. design - 400
2. implementation - 500
3. evaluation - 350
"""
