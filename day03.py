#!/usr/bin/python3
# Day 3 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
input_file = "input.txt"
#input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)

schematic = []
for line in lines:
    schematic.append(list(line))

#-----------------------------------------------------
# Function
#-----------------------------------------------------
# Function used to search for a number in a specified direction (based on x,y coordinates)
def find_number(schematic, x_coordiante, y_coordinate, x_max):
    found_number = 0
    if schematic[y_coordinate][x_coordiante].isnumeric():                       # If character in specified coordinate is a number, check for adjacent numbers
        found_number = schematic[y_coordinate][x_coordiante]
        x_it = x_coordiante - 1
        while x_it >= 0:                                                        # Check left as long as x coordinate is not 0 already
            if schematic[y_coordinate][x_it].isnumeric():                       # Concatenate digets if found
                found_number = schematic[y_coordinate][x_it] + found_number
                schematic[y_coordinate][x_it] = '.'
                x_it -= 1
            else: break
    
        x_it = x_coordiante + 1
        while x_it <= x_max:                                                    # Check right as long as x coordinate is not the max possible
            if schematic[y_coordinate][x_it].isnumeric():                       # Concatenate digits if found
                found_number = found_number + schematic[y_coordinate][x_it]
                schematic[y_coordinate][x_it] = '.'
                x_it += 1
            else: break

        found_number = int(found_number)    # Return integer version of found number
    
    return found_number

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
max_y = len(schematic)-1
max_x = len(schematic[0])-1
found_number = None
part_number_sum = 0
'''
for y,line in enumerate(schematic):                                                 # iterate though grid using x and y variables as coordinates
    for x,point in enumerate(line):
        if point.isnumeric() == False and point !='.':                              # If character that is not a period is found, search around it for number
            if y !=0 and x !=0:                                                     # Always check for grid bounds before searching in any given direction
                part_number_sum += find_number(schematic, x-1, y-1, max_x)          # Search diagonaly up and left        
            if y !=0:
                part_number_sum += find_number(schematic, x, y-1, max_x)            # Search directly above
            if y !=0 and x != max_x:
                part_number_sum += find_number(schematic, x+1, y-1, max_x)          # Search diagonaly up and right
            if x != max_x:
                part_number_sum += find_number(schematic, x+1, y, max_x)            # Search to the right
            if y !=max_y and x != max_x:
                part_number_sum += find_number(schematic, x+1, y+1, max_x)          # Search diagonally down and to the right
            if y !=max_y:
                part_number_sum += find_number(schematic, x, y+1, max_x)            # Search directly down
            if y !=max_y and x != 0:
                part_number_sum += find_number(schematic, x-1, y+1, max_x)          # Search diagonally down and to the left
            if x != 0:
                part_number_sum += find_number(schematic, x-1, y, max_x)            # Search to the left
print("Part 1 Answer:",part_number_sum)
'''
#-----------------------------------------------------
# Part 2
#-----------------------------------------------------                        
gear_ratio_sum = 0
part_number = 0
numbers = []

for y,line in enumerate(schematic):                                         # Same Grid Search mechanic
    for x,point in enumerate(line):
        if point =='*':                                                     # Only look for "*" this time, all other symbols irrelevant
            adjacent_num_count = 0                                          # As you search count how many adjacent numbers are found and store their value in 'numbers' list
            if y !=0 and x !=0:                                             # Always check for grid bounderies before searching in any direction
                part_number = find_number(schematic, x-1, y-1, max_x)       # Search diagonaly up and left
                if part_number > 0:
                    adjacent_num_count += 1
                    numbers.append(part_number)
            if y !=0:                                                       # Search directly above
                part_number = find_number(schematic, x, y-1, max_x)
                if part_number > 0:
                    adjacent_num_count += 1
                    numbers.append(part_number)
            if y !=0 and x != max_x:                                        # Search diagonaly up and right
                part_number = find_number(schematic, x+1, y-1, max_x)
                if part_number > 0:
                    adjacent_num_count += 1
                    numbers.append(part_number)
            if x != max_x:                                                  # Search to the right
                part_number = find_number(schematic, x+1, y, max_x)
                if part_number > 0:
                    adjacent_num_count += 1
                    numbers.append(part_number)
            if y !=max_y and x != max_x:                                    # Search diagonally down and to the right
                part_number = find_number(schematic, x+1, y+1, max_x)
                if part_number > 0:
                    adjacent_num_count += 1
                    numbers.append(part_number)
            if y !=max_y:                                                   # Search directly down
                part_number = find_number(schematic, x, y+1, max_x)
                if part_number > 0:
                    adjacent_num_count += 1
                    numbers.append(part_number)
            if y !=max_y and x != 0:                                        # Search diagonally down and to the left
                part_number = find_number(schematic, x-1, y+1, max_x)
                if part_number > 0:
                    adjacent_num_count += 1
                    numbers.append(part_number)
            if x != 0:                                                      # Search to the left
                part_number = find_number(schematic, x-1, y, max_x)
                if part_number > 0:
                    adjacent_num_count += 1
                    numbers.append(part_number)

            if adjacent_num_count == 2:                 # After searching in all directions check if you have exactly 2 adjacencies. If you do, multiply as instructed
                gear_ratio = 1                          # Variable set to 1 to allow correct multiplication
                for num in numbers:
                    gear_ratio = gear_ratio * num
                gear_ratio_sum += gear_ratio            # Track total sum for answer
            adjacent_num_count = 0                      # Reset common search variables before looping
            numbers = []

print("Part 2 Answer:",gear_ratio_sum)

