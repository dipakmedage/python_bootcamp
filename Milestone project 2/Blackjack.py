import random
suits=('Heart','Diamonds','Spades','Cubs')
rank=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={}
c=2
for i,j in enumerate(rank):   #mistake 1 was forgot enumerate
    if i>8:
        values[j]=10
        if j=='Ace':
           values[j]=11 
    else:
        values[j]=c
        c +=1

playing=True

class Card:
    def __init__(self,suits,rank):
        self.suits=suits
        self.rank=rank
    def __str__(self):
        return self.rank+' of '+self.suits

#continue
class Deck:
    def __init__(self):
        self.deck=[] ##starts with empty list
        for i in suits:
            for j in rank:
                self.deck.append(Card(i,j))  #build card object and add them in list
    def __str__(self):
        deck_comp='' #start with empty string
        for card in self.deck:
            deck_comp +='\n'+card.__str__()
        return deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value +=values[card.rank]
        if card.rank=='Ace':
            self.aces +=1
    def adjust_for_aces(self):
        while self.value>21 and self.aces:
            self.value -=10
            self.aces -=1


test_deck=Deck()
test_deck.shuffle()
test_player=Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())

for card in test_player.cards:
    print(card)
#test_player.value
print(test_player.value)
#continue


class Chips:
    def __init__(self):
        self.total=100 #default by supplier
        self.bet=0
    def win_bet(self):
        self.total +=self.bet
    def lose_bet(self):
        self.total -=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input('How many chips you want to bet?'))
        except ValueError:
            print('Please enter integer')
        else:
            if chips.bet>chips.total:
                print('you dont have enough amount in total ',chips.total)
            else:
                break
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_stand(deck,hand):
    global playing
    while True:
        x=input('Would you hit or stand?')
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            playing=False
        else:
            print('Sorry try again')
            continue
        break
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
    #opening statement
    print('Welcome to blackjack get close to 21 ...dealer hits until he/she reaches 17....aces value can be 1 or 11')

    #create  and shuffle deck and give 2 cards to dealer and player
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #player chips operation
    player_chips=Chips()
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        #prompt player hit or stand
        hit_stand(deck,player_hand)

        #show cards but one from dealer hidden
        show_some(player_hand,dealer_hand)

        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
        #if player do not exceed 21 keep playing
        if player_hand.value<=21:
            while dealer_hand.value<=17:
                hit(deck,dealer_hand)

            #show all cards
            show_all(player_hand,dealer_hand)
             # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)
        
        print("player has total chips remaining ",player_chips.total)

        new_game=input('would you like to play another hand? enter "y" or "n"')

        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print('Thanks for playing')
            c=1
            break
    if c==1:
        break




