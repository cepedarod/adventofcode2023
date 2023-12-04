#!/usr/bin/python3
# Day 4 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
answer = 0

for line in lines:
    card_points = 0     # Variable to track total points scored per card

    winning_nums,your_nums = line.split(" | ")      # split intput into the 2 sets
    winning_nums = winning_nums.split(": ")[1]

    winning_nums = winning_nums.replace("  ", " 0")                         # replace the space before single digit numbers with a 0 (e.g. 9 becomes 09)
    if winning_nums.startswith(" "): winning_nums = '0' + winning_nums[1:]  # same as above but for singe digits at the start of string
    your_nums = your_nums.replace("  ", " 0")                               # Do the same for both data sets
    if your_nums.startswith(" "): your_nums = '0' + your_nums[1:]
    your_nums = your_nums.split(" ")                                        # your_nums is converted to list but winning_numbs is left as string for easy search

    for number in your_nums:
        if number in winning_nums:
            if card_points == 0: card_points = 1
            else: card_points = card_points * 2
        
    answer+= card_points

print("Answer Part 1:", answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
card_tracker = {}       # Dictionary used to track how many of each card number exists. Key is card number, value is quantity of that card

for i,line in enumerate(lines):
    if i not in card_tracker: card_tracker[i] = 1   # If card not yet in tracker, add the original copy
    else: card_tracker[i] += 1                      # If card already in tracker (due to generation from previous cards) add original copy

    card_matches = 1    # Variable set to 1 at start to allow correct iteration on line 61
    winning_nums,your_nums = line.split(" | ")      # split intput into the 2 sets
    winning_nums = winning_nums.split(": ")[1]

    winning_nums = winning_nums.replace("  ", " 0")                         # replace the space before single digit numbers with a 0 (e.g. 9 becomes 09)
    if winning_nums.startswith(" "): winning_nums = '0' + winning_nums[1:]  # same as above but for singe digits at the start of string
    your_nums = your_nums.replace("  ", " 0")                               # Do the same for both data sets
    if your_nums.startswith(" "): your_nums = '0' + your_nums[1:]
    your_nums = your_nums.split(" ")                                        # your_nums is converted to list but winning_numbs is left as string for easy search

    for number in your_nums:
        if number in winning_nums: card_matches += 1
    
    for x in range (i+1,i+card_matches):                # add more of the next cards depending this cards number matches
        if x in card_tracker:                           # Loop wont break (only not run) if there are no card matches (desired)
            card_tracker[x] += card_tracker[i]          # Since each version of current card will +1 the number of subsequent cards generated, you can just add current card count
        else:
            card_tracker[x] = card_tracker[i]
        
answer = sum(card_tracker.values())
print("Answer Part 2: ",answer)