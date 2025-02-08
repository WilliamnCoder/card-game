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

def show_card(card):   #this function shows the cards in the console 
    suit, rank = card
    space = " " if len(rank) == 2 else " "
    print (f"""
        +-------+
        |{rank}     {space}|
        |       |
        |   {suit}   |
        |       |
        |{space}     {rank}|
        +-------+
        """ )   

def main (): # the is the main function where the primary logic is executed and is the entry point of the program
    deck = create_deck()
    while len(deck) > 0:
        try:
            num_cards = int(input(f"\nHow many cards do you want to draw? (Cards left: {len(deck)}): "))
            if num_cards <= 0:
                print("Please enter a positive number.")
                continue
            hand, deck = draw_card(deck, num_cards)
            for card in hand:
                show_card(card)
        except ValueError:
            print("The input is invalid. Please enter a number.")
    
    print("\nWe are out of cards. Thank you for playing!")

if __name__ == "__main__": #this is the entry point check to ensure main() function is initialized only when script is run directly here and not when imported as a module in another script 
    main() #the entry point that starts the program