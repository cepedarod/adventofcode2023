#!/usr/bin/python3
# Day 7 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)
#-----------------------------------------------------
# Function / Classes
#-----------------------------------------------------
# Main class to store info on each hand
class hand():
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = int(bet)
        self.strength = 6               # Ranks strength of hand. 0 being strongest, 6 weakest
        self.strength_map = ''          # stores the strength of each card as a letter in a string. the lower the letter the better
    
    # Define that list of object should be sorted by strength
    def __lt__(self, other):
        return self.strength < other.strength
    
    # Function determines the overall strength of the hand (For part 1)
    def calc_strength(self):
        card_count = {}

        for card in self.cards:                             # Record the quantity of each card in hand
            if card in card_count: card_count[card] +=1
            else: card_count[card] = 1

        card_quantities = list(card_count.values())
        card_quantities.sort(reverse=True)                  # Make list of only the card quantities and sort it from most to least

                                                                                        # Check for each potential hand
        if card_quantities[0] == 5: self.strength = 0                                       # five of a kind
        elif card_quantities[0] == 4: self.strength = 1                                     # 4 of a kind
        elif card_quantities[0] == 3 and card_quantities[1] == 2: self.strength = 2         # Full house
        elif card_quantities[0] == 3: self.strength = 3                                     # 3 of a kind
        elif card_quantities[0] == card_quantities[1] == 2: self.strength = 4               # 2 pairs
        elif card_quantities[0] == 2: self.strength = 5                                     # 1 pair
                                                                                            # high card already assumed on init
    # Calculate strength of hand but account for jokers
    def calc_strength_part2(self):
        card_count = {}
        j_num = 0

        for card in self.cards:
            if card =='J': j_num += 1                           # If card is a joker, count seperatly
            elif card in card_count: card_count[card] +=1       # Otherwise count as before
            else: card_count[card] = 1

        card_quantities = list(card_count.values())
        card_quantities.sort(reverse=True)
        
        if j_num == 5:                                          # If all cards in hand are jokers, hand = five of a kind
            self.strength = 0
            return
        card_quantities[0] += j_num                             # Else add the number of jokers to the count for the most abundant card in hand

        if card_quantities[0] == 5: self.strength = 0           # Check hand composition as detailed in the previous function
        elif card_quantities[0] == 4: self.strength = 1
        elif card_quantities[0] == 3 and card_quantities[1] == 2: self.strength = 2
        elif card_quantities[0] == 3: self.strength = 3
        elif card_quantities[0] == card_quantities[1] == 2: self.strength = 4
        elif card_quantities[0] == 2: self.strength = 5
    
    # convert hand into a string that details the priority of each card to break ties
    # function takes a deck orderd to accomodate prompt
    def make_strength_map(self, deck):
        card_to_strength_map = ['A','B','C','D','E','F','G','H','I','J','K','L','M']    # Card numbers are converted to letters. smaller letter = Better card
        s = ''
        for card in self.cards:                           # convert each card in hand to reference letter from above list
            for i, ref in enumerate(deck):
                if card == ref:
                    s += card_to_strength_map[i]
                    break
        
        self.strength_map = s

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
deck = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
hands = []
rank_it = len(lines)    # Max Rank value for hand
answer = 0

# Convert Raw input into list of hand objects
for line in lines:
    cards, bet = line.split(" ")
    new_hand = hand(cards, bet)
    new_hand.calc_strength()            # Calculate strength of hand
    new_hand.make_strength_map(deck)    # Calculate tie breaker values
    hands.append(new_hand)

hands.sort(key=lambda x: (x.strength, x.strength_map))  # Sort list of hands first on strength then on card tie breaker

# Calculate answer
for hand in hands:
    answer += hand.bet * rank_it
    rank_it -= 1

print("Part 1 Answer: ", answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
deck_2 = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']  # Deck has joker as worst tie break value now
answer = 0

# Re-calculate strength based on part 2 parameters
for hand in hands:
    hand.calc_strength_part2()
    hand.make_strength_map(deck_2)

hands.sort(key=lambda x: (x.strength, x.strength_map))      # Re-sort

rank_it = len(lines)
for hand in hands:
    answer += hand.bet * rank_it
    rank_it -= 1

print("Part 2 Answer: ", answer)