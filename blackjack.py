import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return "%s of %s" %(self.suit, self.rank)
        #print(self.rank)

#c=Card(suit=suits[0],rank=ranks[0])
#print(c)

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        #Deck.shuffle(self)
        for d in self.deck:
            print(d)
        return "all the cards in this deck"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)

    def adjust_for_ace(self):
        for c in self.cards:
            self.value+=values[c.rank]
            if c.rank=='Aces':
                if self.value>21:
                    self.value-=10
        return self.value

class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

    def take_bet(bets):
        self.bet=bets

def comparedealer(points):
    if points==21:
        return True
    else:
        return False

def printcards(hand):
    for card in hand.cards[]:
        print(card)



while True:
    playerpoint=0
    dealerpoint=0
    hityn=""
    # Print an opening statement


    # Create & shuffle the deck, deal two cards to each player
    deck1=Deck()
    deck1.shuffle()
    dealerhand=Hand()
    dealerhand.add_card(deck1.deal())
    dealerhand.add_card(deck1.deal())
    dealerpoint=dealerhand.adjust_for_ace()
    print("dealer's hand")
    print("??????????")
    print(dealerhand.card[1])
    playerhand=Hand()
    playerhand.add_card(deck1.deal())
    playerhand.add_card(deck1.deal())
    playerpoint=playerhand.adjust_for_ace()
    print("player's hand")
    print(playerhand.card[0])
    print(playerhand.card[1])
    # Set up the Player's chips
    playerchip=Chips()

    # Prompt the Player for their bet
    playerchip.take_bet(int(input("Player enter your bet please(1~100):")))

    # Show cards (but keep one dealer card hidden)
    print("dealer's card: ????????? , %s" % dealerhand.cards[1]))
    print("player's card: %s, %s" %(playerhand.cards[0], playerhand.cards[1]))
    if playerpoint==21:
        if dealerpoint==21:
            print('tie, player and dealer both have 21 ')
            print("dealer's card: %s , %s" %(dealerhand.cards[0],dealerhand.cards[1]))
            print("player has %s chips now" % playerchip.total)
        else:
            print('player wins')
            print("dealer's card: %s , %s" % (dealerhand.cards[0],dealerhand.cards[1]))
            playerchip.win_bet()
            print("player has %s chips now" % playerchip.total)
    else:
        while playerpoint<21:
            hityn=input("Hit?(y or n): ")
            if hityn=="y":
                playerhand.add_card(deck1.deal())
                playerpoint=playerhand.adjust_for_ace()
                print("player's card: ")
                printcards(playerhand)
                if playerpoint<21:
                    continue
                elif playerpoint==21:
                    if comparedealer(dealerpoint):
                        print('tie, player and dealer both have 21 ')
                        print("dealer's card: ")
                        printcards(dealerhand)
                        print("player has %s chips now" % playerchip.total)
                    else:
                        print('player wins')
                        print('dealer\'s cards:')
                        printcards(dealerhand)
                        playerchip.win_bet()
                        print("player has %s chips now" % playerchip.total)

                else:
                    print('player busts')
                    playerchip.lose_bet()
                    print("player has %s chips now" % playerchip.total)

            elif hityn=="n":
                while dealerpoint<17 and dealerpoint<playerpoint:
                    dealerhand.add_card(deck1.deal())
                    printcards(dealerhand)
                    dealerpoint=dealerhand.adjust_for_ace()
                if dealerpoint>21:
                    print("dealer busts!")
                    printcards(dealerhand)
                    playerchip.win_bet()
                    print("player has %s chips now" % playerchip.total)
                elif dealerpoint==21:
                    print('dealer has blackjack!')
                    playerchip.lose_bet()
                    print("player has %s chips now" % playerchip.total)
                elif dealerpoint<21 and dealerpoint>playerpoint:
                    print('dealer wins')
                    playerchip.lose_bet()
                    print("player has %s chips now" % playerchip.total)

    againyn=input("play again? (y/n)")
    if againyn=="y":
        continue
    elif againyn=="n":
        sys.exit()
