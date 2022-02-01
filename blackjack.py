from itertools import count
import random 

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return f"({self.value} of {self.suit})"
    
def get_cards():
    cards = []
    suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for suit in suits:
        for value in values:
            card = Card(suit, value)
            cards.append(card)
    return cards


class Deck:
    def __init__(self):
        self.cards = get_cards()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, player):
        card = self.cards.pop(0)
        player.hand.append(card)

    
class Player:
    def __init__(self):
        self.hand = []

    def count_hand(self):
        count = 0
        for card in self.hand:
            count += card.value
        return count


class Dealer(Player):
    def __init__(self):
        super().__init__()

    def show_hand(self):
        s = "Dealer has... "
        for idx, card in enumerate (self.hand):
            if idx == 0:
                s += "(???) "
            else:
                s += f"{card} "
        print(s)
         


class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def show_hand(self):
        print(f"{self.name} has {self.hand} ")

class Game:
    def __init__(self, player, dealer, deck) -> None:
        self.player = player
        self.dealer = dealer
        self.deck = deck
        

    def run(self):
         print(f"Welcome to BlackJack! ")
         print("The goal is to get as close to 21 without going over. ")
         print("Let's play! ")
        # shuffle cards
         self.deck.shuffle()
         print("* The cards have been shuffled * ")
         print("Deal is up! ")
        # deal 2 cards to each player
         print("...and the first card is:")
         
         self.deck.deal(self.player)
         self.deck.deal(self.dealer)
        

         self.player.show_hand()
         self.dealer.show_hand()
         print("...and the second card is: ")
         self.deck.deal(self.player)
         self.deck.deal(self.dealer)

         self.player.show_hand()
         self.dealer.show_hand()
         print(f"==" * 20)
      
         
         running = True
         while True:
            # user input would you like to hit or stand
            if self.player.count_hand() > 21:
                print("In real BlackJack this is impossible, but this isnt real BlackJack. You lose! ")
            print(f"You currently have : {self.player.count_hand()}")
            print(f"==" * 20)
            answer = input(f"Would you like to Hit (H) or Stand (S) ").lower()
            if answer == "h":
                self.deck.deal(self.player)
                self.player.show_hand()
                print(self.player.count_hand())
                if self.player.count_hand() > 21:
                    print(f"You bust! Better luck next time.")
                    return
            elif answer == "s":     ######### THIS SCENARIO BREAKS THE GAME sometimes?
                break
         while True:
          if self.dealer.count_hand() < 18:
            print("Dealer hits!")
            self.deck.deal(self.dealer)
            self.dealer.show_hand()
          elif self.dealer.count_hand() > 18:
            print("Dealer stays.")
            break
        
         print(f"You had : {self.player.count_hand()} ")
         print(f"Dealer had: {self.dealer.count_hand()} ")
         
         if self.dealer.count_hand() > 21:
             print(f"Dealer busts with {self.dealer.count_hand()}!")
             print(f"You won! ")
         elif self.dealer.count_hand() > self.player.count_hand():
             print(f"You lose! ")
    
         else:
             print(f"Congrats, you won! ")
                           
    

def main():
    player = Human("Player")
    dealer = Dealer()
    deck = Deck()
    game = Game(player, dealer, deck)
    
    game.run()

main()

                


    
    












       


        






