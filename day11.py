#!/usr/bin/python3
# Day 11 Puzzle

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
def print_map(map):
    l = ''
    for row in map:
        for point in row:
            l += str(point)
        print(l)
        l = ''

# Applies part 1 expansion rules to map
def expand_map(map):
    empty_index = []

    for x, row in enumerate(map):
        if all(i == row[0] for i in row) and row[0] == ".":
            empty_index.append(x)

    expansion_factor = 0
    for row in empty_index:
        new_row = ['.'] * len(map[0])
        map.insert(row + expansion_factor, new_row)
        expansion_factor +=1


    it = 0
    empty = True
    empty_index = []
    while it < len(map[0]):
        for row in map:
            if row[it] == "#":
                empty = False
                break
        
        if empty: 
            empty_index.append(it)
        it += 1
        empty = True

    expansion_factor = 0
    for it in empty_index:
        for row in map:
            row.insert(it + expansion_factor, '.')
        expansion_factor +=1

def calc_distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

# map indexes of empty rows and columns in map
def empty_rows_and_columns(map):
    empty_rows = []

    for x, row in enumerate(map):
        if all(i == row[0] for i in row) and row[0] == ".":
            empty_rows.append(x)

    it = 0
    empty = True
    empty_columns = []
    while it < len(map[0]):
        for row in map:
            if row[it] == "#":
                empty = False
                break
        
        if empty: 
            empty_columns.append(it)
        it += 1
        empty = True

    return empty_rows, empty_columns

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
map = []
for line in lines:
    map.append(list(line))

expand_map(map)     # add extra rows and columns

# make a list with all the coordinates of all galaxies
known_galaxies = []
galaxy_num = 0
for y, row in enumerate(map):
    for x, point in enumerate(row):
        if point == "#": known_galaxies.append([x,y])

#print_map(map)     # Debug

# Calculate distance between galaxies
answer = 0
for i, galaxy in enumerate(known_galaxies):
    start = i + 1
    for next_g in known_galaxies[start:]:
        dist = calc_distance(galaxy, next_g)
        answer += dist
        #print(f"{galaxy} --> {next_g}: {dist}")            # Debug
    #print(f"------{answer}------")                         # Debug

#print(known_galaxies)                                      # Debug
print("Part 1 Answer:", answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
original_map = []           # Answer needs to be caluclated numeric, so take original values
for line in lines:
    original_map.append(list(line))

#print_map(original_map)    # Debug

# find indexes of all empty rows and columns
empty_rows, empty_columns = empty_rows_and_columns(original_map)

# note original coordinates of galaxies
for galaxy in known_galaxies:
    og_x = galaxy[0]
    og_y = galaxy[1]

    # For each empty row above galaxy add 1M to its y coordinate
    for row in empty_rows:
        if og_y > row:
            galaxy[1] += 1000000 - 1
        else: break

    # For each empty column to the left of galaxy add 1M to its x coordinate
    for column in empty_columns:
        if og_x > column:
            galaxy[0] += 1000000 - 1
        else: break

#print(known_galaxies)

# Calculate distances
answer = 0
for i, galaxy in enumerate(known_galaxies):
    start = i + 1
    for next_g in known_galaxies[start:]:
        dist = calc_distance(galaxy, next_g)
        answer += dist

print("Part 2 Answer: ", answer)




 





