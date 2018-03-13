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

c=Card(suit=suits[0],rank=ranks[0])
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
        return self.deck.pop()

testdeck=Deck()
print(testdeck)

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

def hit(deck,hand):

    pass
while True:
    # Print an opening statement


    # Create & shuffle the deck, deal two cards to each player
    deck1=Deck()
    deck1.shuffle()
    dealerhand=Hand()
    dealerhand.add_card(deck1.deal())
    dealerhand.add_card(deck1.deal())
    print("dealer's hand")
    print("??????????")
    print(dealerhand.card[1])
    playerhand=Hand()
    playerhand.add_card(deck1.deal())
    playerhand.add_card(deck1.deal())
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
    if playerhand.adjust_for_ace()==21:
        if dealerhand.adjust_for_ace()==21:
            print('tie, player and dealer both have 21 ')
            print("dealer's card: %s , %s" %(dealerhand.cards[0],dealerhand.cards[1]))
            print("player has %s chips now" % playerchip.total)
        else:
            print('player wins')
            print("dealer's card: %s , %s" % (dealerhand.cards[0],dealerhand.cards[1]))
            playerchip.win_bet()
            print("player has %s chips now" % playerchip.total)
    else:

    while playing:  # recall this variable from our hit_or_stand function


        # Prompt for Player to Hit or Stand

        # Show cards (but keep one dealer card hidden)


        # If player's hand exceeds 21, run player_busts() and break out of loop


            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17


        # Show all cards

        # Run different winning scenarios


    # Inform Player of their chips total

    # Ask to play again

        break
