import random

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value


class Deck:
    z = 0
    newDeck = []
    suitlist = ["Hearts", "Diamonds", "Clubs", "Spades"]
    namelist = ["Ace of","two of","three of","four of","five of","six of","seven of","eight of","nine of","ten of","jack of","queen of","king of"]
    for x in suitlist:
        z = 0
        for j in namelist:
            if z < 10:
                z += 1
            else:
                z = 10
            newCard = Card(j,x,z)
            newDeck.append(newCard)
            

#used for checking the entire deck for debugging and why not purposes
def checkDeck():
    x = len(Deck.newDeck)
    for n in range (0,x,1):
        printIt = Deck.newDeck[n]
        print (printIt)

def checkHand(playerHand):
    x = len(playerHand)
    for i in range (0,x,1):
        print (playerHand[i].name, playerHand[i].suit)
    return

def checkPool(betPool):
    print (betPool)
    return

def checkMoney(userMoney):
    print (userMoney)
    return

def dealACard():
    dealtCard = Deck.newDeck[0]
    del Deck.newDeck[0]
    #print (dealtCard.name,dealtCard.suit,dealtCard.value)
    return dealtCard


def shuffDeck ():
    shuffset = random.shuffle(Deck.newDeck)
    return Deck.newDeck

def addMoney(userMoney):
    try:
        moneyAddAmt = input("Input $ amt to add: ")
        moneyAddAmt = int(moneyAddAmt)
        userMoney += moneyAddAmt
        return userMoney
    except:
        return userMoney

def initialBet (userMoney,betPool):
        try:
            print("add money")
            userMoney = addMoney(userMoney)
            betAmt = input("Bet amount: ")
            betAmt = int(betAmt)
            userMoney -= betAmt
            betPool += betAmt
            return userMoney,betPool
        except:
            return userMoney,betPool


def initialDeal(playerHand, dealerHand):
    shuffDeck()
    playerHand.append (dealACard())
    dealerHand.append (dealACard())
    playerHand.append (dealACard())
    dealerHand.append (dealACard())
    x = len(playerHand)
    for i in range (0,x,1):
        print (playerHand[i].name, playerHand[i].suit)
    print ("dealer first card:",dealerHand[0].name, dealerHand[0].suit)
    return playerHand,dealerHand

def descision(playerHand, dealerHand, turn, dealerChoice,done):
    
    print ("Hit = H", "Stand = S",)
    if turn %2 != 0:
        if dealerChoice == 1:
            inpValue = "S"
            done = 1
            print (inpValue)
        if dealerChoice == 2:
            inpValue = "H"
            print (inpValue)
            dealerHand.append (dealACard())
    else:
        inpValue = input("What would you like to do? ")
        if inpValue == "S":
            done = 1
            return done
        if inpValue == "H":
            playerHand.append (dealACard())
            y = len(playerHand)
            for p in range (0,y,1):
                print (playerHand[p].name, playerHand[p].suit)       

        return done

def checkWin (playerHand, dealerHand):
    x = len(playerHand)
    pHandValue = 0
    for i in range (0,x,1):
        y = int(playerHand[i].value)
        pHandValue += y
        if pHandValue > 21:
            Win = 1
            print ("you busted")
            quit()
            
        
    a = len(dealerHand)
    dHandValue = 0
    for p in range (0,a,1):
        b = int(dealerHand[p].value)
        dHandValue += b
        if dHandValue > 21:
            Win = 1
            print ("Dealer busted")
            quit()

    return pHandValue,dHandValue

def main():
    userMoney = 0
    betPool = 0
    playerHand = []
    dealerHand = []
    turn = 0
    Win = 0
    playerHand.clear()
    dealerHand.clear()
    dealerChoice = 0
    done = 0
    pHandValue = 0
    dHandValue = 0

    nextStep = 0
    userMoney,betPool = initialBet(userMoney,betPool)
    initialDeal(playerHand,dealerHand)
    while Win == 0:

        pHandValue,dHandValue = checkWin(playerHand,dealerHand)

        if turn %2 == 0:
            while nextStep == 0:
                print ("type money add, to add money, end to end, check Hand to check your hand, check money to check you balance check pot to check the amount of money in the pot, and continue to move on: ")
                masterInput = input()
                
                if masterInput == "money add":
                    userMoney = addMoney(userMoney)
                    
                if masterInput == "check hand":
                    checkHand(playerHand)

                if masterInput == "check pot":
                    checkPool(betPool)

                if masterInput == "check money":
                    checkMoney(userMoney)

                if masterInput == "continue":
                    nextStep = 1

                if masterInput == "end":
                    quit()

        else:
            if pHandValue > dHandValue:
                dealerChoice = 2
            else:
                print ("dealer stood","dealer won")
                x = len(dealerHand)
                for i in range (0,x,1):
                    print (dealerHand[i].name, dealerHand[i].suit)
                quit()
            done = descision(playerHand,dealerHand,turn,dealerChoice,done)
            x = len(dealerHand)
            for i in range (0,x,1):
                print (dealerHand[i].name, dealerHand[i].suit)
        if done == 1:
            turn += 1
            print ("yup finished")
        else:
            if nextStep == 1:
                
                done = descision(playerHand,dealerHand,turn,dealerChoice,done)
        print ("","turn: ",turn,"")
        
    return
        


main()