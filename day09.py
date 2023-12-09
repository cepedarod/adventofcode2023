#!/usr/bin/python3
# Day 9 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)
#-----------------------------------------------------
# Functions
#-----------------------------------------------------
# Convert items in list to ints
def make_ints(list):
    new_list = []
    for x in list: new_list.append(int(x))

    return new_list

# Check if all elements in a list are the same
def all_same(list):
    return all(i == list[0] for i in list)

# Make a new sequence by taking the difference between the values of the provided sequence
def find_next_sequence(sequence):
    it = 1
    new_sequence = []
    while it < len(sequence):
        new_sequence.append(sequence[it]-sequence[it-1])
        it += 1
    
    return new_sequence

# Calculate next value in a sequence using the sequence history
def next_value(sequence_history):
    seq_modifier = sequence_history[-1][-1]
    sequence_history[-1].append(seq_modifier)

    for seq in reversed(sequence_history[:-1]):
        seq_modifier = seq[-1] + seq_modifier
        seq.append(seq_modifier)

    return seq_modifier

# Calculate the previous value in a sequence using the sequence history
def prev_value(sequence_history):
    seq_modifier = sequence_history[-1][0]
    sequence_history[-1].insert(0, seq_modifier)

    for seq in reversed(sequence_history[:-1]):
        seq_modifier = seq[0] - seq_modifier
        seq.insert(0, seq_modifier)
    
    return seq_modifier

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
answer = 0
for line in lines:
    sequence_history = []
    sequence = line.split(" ")
    sequence = make_ints(sequence)
    sequence_history.append(sequence)
    next_seq = sequence
    rock_bottom = False                 # Determines if the all-zeros sequence has been found

    while not rock_bottom:
        next_seq = find_next_sequence(next_seq)
        sequence_history.append(next_seq)

        if all_same(next_seq) and next_seq[0] == 0: rock_bottom = True

    
    answer += next_value(sequence_history)
    #for seq in sequence_history: print(seq)        # Debug

print("Part 1 Answer: ", answer)
    
#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
answer = 0
for line in lines:
    sequence_history = []
    sequence = line.split(" ")
    sequence = make_ints(sequence)
    sequence_history.append(sequence)
    next_seq = sequence
    rock_bottom = False

    while not rock_bottom:
        next_seq = find_next_sequence(next_seq)
        sequence_history.append(next_seq)

        if all_same(next_seq) and next_seq[0] == 0: rock_bottom = True

    
    answer += prev_value(sequence_history)          # Only difference from part 1
    #for seq in sequence_history: print(seq)        # Debug

print("Part 2 Answer: ", answer)