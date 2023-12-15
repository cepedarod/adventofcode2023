#!/usr/bin/python3
# Day 14 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)
#-----------------------------------------------------
# Function
#-----------------------------------------------------
def print_array(array):
    for row in array:
        l = ''
        for point in row:
            l += point
        print(l)

def sum_points_old(sideways_array):
    total = 0
    for column in sideways_array:
        for i, point in enumerate(column):
            if point == "O":
                total+= (len(column) - i)
        
    return total

def sum_points(array):
    total = 0
    for i,row in enumerate(array):
        for point in row:
            if point == "O": total+= (len(array) - i)

    return total

def flip_clockwise(array):
    return list(zip(*array[::-1]))

def correct_orientation(sideways_array):
    return list(zip(*sideways_array))

def tumble_north(array):
    col_it = 0
    new_array = []
    while col_it < len(array[0]):
        new_col = []
        for y, row in enumerate(array):
            if row[col_it] == "O": new_col.append("O")
            elif row[col_it] == "#":
                sequence = ["."] * (y - len(new_col))
                sequence.append("#")
                new_col.extend(sequence)

        missing_chunk = ["."] * (len(array) - len(new_col))
        new_col.extend(missing_chunk)
        new_array.append(new_col)
        col_it += 1
    
    new_array = correct_orientation(new_array)
    return new_array

def spin_cycle(array):
    current_array = array.copy()
    current_array = tumble_north(current_array)
    current_array = correct_orientation(current_array)
    #print_array(current_array)
    current_array = flip_clockwise(current_array)
    current_array = tumble_north(current_array)
    current_array = correct_orientation(current_array)
    #print_array(current_array)
    #print("------------------")
    current_array = flip_clockwise(current_array)
    current_array = tumble_north(current_array)
    current_array = correct_orientation(current_array)
    #print_array(current_array)
    #print("------------------")
    current_array = flip_clockwise(current_array)
    current_array = tumble_north(current_array)
    current_array = correct_orientation(current_array)

    current_array = flip_clockwise(current_array)
    #print_array(current_array)
    #print("------------------")
    #print("------------------")

    return current_array

def array_to_string(array):
    s = ''
    for row in array:
        for point in row:
            s += point

    return s

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
array = []

for line in lines:
    array.append(list(line))

'''
new_array = array.copy()
new_array = tumble_north(new_array)

#new_array = correct_orientation(new_array)
#print_array(new_array)
print("Answer Part 1: ", sum_points(new_array))
'''
#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
known_array_configs = {}
it = 0
current_array = array.copy()
remaining_tumbles = 1000000000
found_loop = False

while it < remaining_tumbles:
    current_array = spin_cycle(current_array)
    array_hash = array_to_string(current_array)
    
    it+= 1
    if array_hash in known_array_configs and found_loop == False:
        cycle_frequency = it - known_array_configs[array_hash]
        remaining_tumbles = (remaining_tumbles - it) % cycle_frequency
        it = 0
        found_loop = True
    elif found_loop == False: 
        known_array_configs[array_hash] = it
        #print_array(current_array)
        #print("------------------")

#print_array(current_array)
debug = 0
print("Answer Part 2: ", sum_points(current_array))

