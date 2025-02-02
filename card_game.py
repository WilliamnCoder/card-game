import random  # this module is imported because it includes randomness necessary for the shuffling of the deck of cards

def draw_card(deck, num_cards):  # this function takes the parameters deck (a list of cards) and num_cards (number of cards)
    if num_cards > len(deck): #if the number of cards requested exceeds number of cards left in the deck the following code line will be true
        print(f"Cannot draw {num_cards} cards. Only {len(deck)} cards left.") #if the if-condition is true, this is printed
        num_cards = len(deck) #this guarantees that number of cards that is left don't exceed the length of cards that is left
    hand = [deck.pop() for _ in range (num_cards)] #list comprehension that iterates through num_cards and pops (removes) from the deck and adds it to the hand.
    return hand, deck #this returns the list of drawn cards (hand) and remaining cards (deck)

def create_deck(): #the function creates a full deck of cards (52)
    suits = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck) # this introduces randomness into the deck of cards
    return deck

