#!/usr/bin/python3
# Day 10 Puzzle
#-----------------------------------------------------
# Imports
#-----------------------------------------------------
import sys
sys.setrecursionlimit(45000)   # Needed to facilitate recursion depth leveraged for part 2
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
# determines what 2 pipes are connected to the start point.
# Function returns a dict with the cardinal direction the S is to the adjacent pipe and the pipes xy coordinates
def find_endpoints(map, start_xy, max_x, max_y):
    x = start_xy[0]
    y = start_xy[1]
    viable_connectors = {}

    if y !=0 and (map[y-1][x] == '|' or map[y-1][x] == '7' or map[y-1][x] == 'F'):
        viable_connectors['s'] = (x, y-1)                                                  # Search directly above
    if x != max_x and (map[y][x+1] == '-' or map[y][x+1] == 'J' or map[y][x+1] == '7'):
        viable_connectors['w'] = (x+1, y)                                                  # Search to the right
    if y !=max_y and (map[y+1][x] == 'L' or map[y+1][x] == 'J' or map[y+1][x] == '|'):
        viable_connectors['n'] = (x, y+1)                                                  # Search directly down
    if x != 0 and (map[y][x-1] == '-' or map[y][x-1] == 'L' or map[y][x-1] == 'F'):
        viable_connectors['e'] = (x-1, y)                                                  # Search to the left

    return viable_connectors

# determine what type of pipe the S is
def start_shape (viable_connectors):
    if 'n' in viable_connectors and 's' in viable_connectors: return '|'
    elif 'e' in viable_connectors and 'w' in viable_connectors: return '-'
    elif 'n' in viable_connectors and 'w' in viable_connectors: return 'F'
    elif 'n' in viable_connectors and 'e' in viable_connectors: return '7'
    elif 's' in viable_connectors and 'w' in viable_connectors: return 'L'
    elif 's' in viable_connectors and 'e' in viable_connectors: return 'J'
    
# Make map that only shows the actual characted for the pipe. converts everything else to a '.'
def make_visual(map, v_map, x_start, y_start, origin):
    x = x_start
    y = y_start
    node = map[y][x]
    length = 1
    new_map = v_map
    
    while node != 'S':
        length += 1
        new_map[y][x] = node

        if node == '|' and origin == "n": 
            node = map[y+1][x]
            y+=1
            origin = 'n'
        elif node == '|' and origin == "s": 
            node = map[y-1][x]
            y-=1
            origin = 's'
        elif node == '-' and origin == "e": 
            node = map[y][x-1]
            x-=1
            origin = 'e'
        elif node == '-' and origin == "w": 
            node = map[y][x+1]
            x+=1
            origin = 'w'
        elif node == 'L' and origin == "n": 
            node = map[y][x+1]
            x+=1
            origin = 'w'
        elif node == 'L' and origin == "e": 
            node = map[y-1][x]
            y-=1
            origin = 's'
        elif node == 'J' and origin == "n": 
            node = map[y][x-1]
            x-=1
            origin = 'e'
        elif node == 'J' and origin == "w": 
            node = map[y-1][x]
            y-=1
            origin = 's'
        elif node == '7' and origin == "s": 
            node = map[y][x-1]
            x-=1
            origin = 'e'
        elif node == '7' and origin == "w": 
            node = map[y+1][x]
            y+=1
            origin = 'n'
        elif node == 'F' and origin == "s": 
            node = map[y][x+1]
            x+=1
            origin = 'w'
        elif node == 'F' and origin == "e": 
            node = map[y+1][x]
            y+=1
            origin = 'n'
        elif node == '.':
            print("Error: hit . in loop")
            return length
        
    return new_map

# prints map
def print_visual(visual_map):
    for row in visual_map:
        line = ''
        for point in row: line += point
        print(line)

# determines length of pipe loop
def loop_length(map, x_start, y_start, origin):
    x = x_start
    y = y_start
    node = map[y][x]
    length = 1          # Account for S
    
    while node != 'S':
        length += 1

        if node == '|' and origin == "n": 
            node = map[y+1][x]
            y+=1
            origin = 'n'
        elif node == '|' and origin == "s": 
            node = map[y-1][x]
            y-=1
            origin = 's'
        elif node == '-' and origin == "e": 
            node = map[y][x-1]
            x-=1
            origin = 'e'
        elif node == '-' and origin == "w": 
            node = map[y][x+1]
            x+=1
            origin = 'w'
        elif node == 'L' and origin == "n": 
            node = map[y][x+1]
            x+=1
            origin = 'w'
        elif node == 'L' and origin == "e": 
            node = map[y-1][x]
            y-=1
            origin = 's'
        elif node == 'J' and origin == "n": 
            node = map[y][x-1]
            x-=1
            origin = 'e'
        elif node == 'J' and origin == "w": 
            node = map[y-1][x]
            y-=1
            origin = 's'
        elif node == '7' and origin == "s": 
            node = map[y][x-1]
            x-=1
            origin = 'e'
        elif node == '7' and origin == "w": 
            node = map[y+1][x]
            y+=1
            origin = 'n'
        elif node == 'F' and origin == "s": 
            node = map[y][x+1]
            x+=1
            origin = 'w'
        elif node == 'F' and origin == "e": 
            node = map[y+1][x]
            y+=1
            origin = 'n'
        elif node == '.':
            print("Error: hit . in loop")
            return length
        
    return length

# represents original carcters as 3 '#' caracters in a 3x3 grid
# Converts map into a 9x bigger map that has real shape representation
def convert(top_left_x, top_left_y, bigger_map, point):
    x = top_left_x
    y = top_left_y
    if point == '|':
        bigger_map[y][x+1] = "#"
        bigger_map[y+1][x+1] = "#"
        bigger_map[y+2][x+1] = "#"
    elif point == "-":
        bigger_map[y+1][x] = "#"
        bigger_map[y+1][x+1] = "#"
        bigger_map[y+1][x+2] = "#"
    elif point == "L":
        bigger_map[y][x+1] = "#"
        bigger_map[y+1][x+1] = "#"
        bigger_map[y+1][x+2] = "#"
    elif point == "J":
        bigger_map[y][x+1] = "#"
        bigger_map[y+1][x] = "#"
        bigger_map[y+1][x+1] = "#"
    elif point == "7":
        bigger_map[y+1][x] = "#"
        bigger_map[y+1][x+1] = "#"
        bigger_map[y+2][x+1] = "#"
    elif point == "F":
        bigger_map[y+1][x+1] = "#"
        bigger_map[y+1][x+2] = "#"
        bigger_map[y+2][x+1] = "#"
    elif point == ".":
        bigger_map[y+1][x+1] = "x"

# recursively deletes any points that can be reached from the current point
# if started from outside loop will delete all points not inside pipe loop
def purge(x, y, map):
    if map[y][x] != "#" and map[y][x] != " "  :
        map[y][x] = ' '

        if x != 0: purge(x-1, y, map)
        if y != 0: purge(x, y-1, map)
        if x < len(map[0]) - 1: purge(x+1, y, map)
        if y < len(map) - 1: purge(x, y+1, map)

    return

# reduces map size by getting rid of empty fringe lines
# needed to reduce load on recursion
def trim(map):
    map_it = map.copy()

    for row in map_it:
        if "#" not in row: map.pop(0)
        else: break

    for row in reversed(map_it):
        if "#" not in row: map.pop()
        else: break

    map_it = map.copy()
    it = 0
    empty = True
    debug = 0
    found_edge = False
    while not found_edge:
        for row in map:
            if row[it] == '#':
                found_edge = True 
                break
        if not found_edge: it+=1

    i = 0
    while i < it:
        debug += 1
        for row in map:
            row.pop(0)
        i += 1

    map_it = map.copy()
    it = 0
    empty = True
    debug = 0
    found_edge = False
    while not found_edge:
        for row in map:
            row_r = list(reversed(row))
            if row_r[it] == '#':
                found_edge = True 
                break
        if not found_edge: it+=1

    i = 0
    while i < it:
        debug += 1
        for row in map:
            row.pop()
        i += 1

#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
map = []            # OG Values
visual_map = []     # Cleaned up values
for line in lines:
    map.append(list(line))
    v_line = ['.'] * len(list(line))
    visual_map.append(v_line)

max_y = len(map) - 1
max_x = len(map[0]) - 1

start_xy = ''
S_shape = ''
for y, row in enumerate(map):
    for x, point in enumerate(row):
        if point == 'S':
            start_xy = (x,y)                                                    # Location of S
            viable_connectors = find_endpoints(map, start_xy, max_x, max_y)     # Determine x_y and shape of connection points
            visual_map[y][x] = 'S'
            S_shape = start_shape (viable_connectors)                           # Replace S with real shape
            break
    
    if start_xy: break

# Pick coordinates of one of the pipes connected to S and measure length of loop
origin = list(viable_connectors.keys())[0]  
total_length = loop_length(map, viable_connectors[origin][0], viable_connectors[origin][1], origin)

print("Answer Part 1: ", total_length / 2)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
visual_map = make_visual(map, visual_map, viable_connectors[origin][0], viable_connectors[origin][1], origin)
#print_visual(visual_map)       # Debug

visual_map[start_xy[1]][start_xy[0]] = S_shape
#print_visual(visual_map)       # Debug

# Make map 9x size of original to acommodate better shape definition
expanded_map = []
for row in visual_map:
    expanded_row = ["."] * len(row) * 3
    expanded_row2 = ["."] * len(row) * 3
    expanded_row3 = ["."] * len(row) * 3
    expanded_map.append(expanded_row)
    expanded_map.append(expanded_row2)
    expanded_map.append(expanded_row3)
 
 # represent loop in bigger map using '#'
expanded_y = 0
expanded_x = 0
for y, row in enumerate(visual_map):
    for x, point in enumerate(row):
        convert(expanded_x, expanded_y, expanded_map, point)
        expanded_x += 3
    expanded_x = 0 
    expanded_y += 3

trim (expanded_map)                 # Get rid of empty space in edges
#print_visual(expanded_map)         # Debug

# Run purge funcition in stages to avoid crashing from excessive recursion
checkpoint_found = False
for i, line in enumerate(expanded_map):
    if checkpoint_found == True and line[0] != '#':
        purge(0, i, expanded_map)
    
    elif checkpoint_found == False and line[0] == '#':
        checkpoint_found = True
        purge(0, i-1, expanded_map)

checkpoint_found = False
for i, line in enumerate(expanded_map):
    if checkpoint_found == True and line[0] != '#':
        purge(0, i, expanded_map)
    
    elif checkpoint_found == False and line[0] == '#':
        checkpoint_found = True
        purge(0, i-1, expanded_map)

purge(len(expanded_map[0])- 50, 0, expanded_map)
purge(len(expanded_map[0])- 50, len(expanded_map)-1, expanded_map)

for i, point in enumerate(expanded_map[0]):
    if point == '.' or point == 'x':
        purge(i, 0, expanded_map)

print_visual(expanded_map)      # Print map cuz why not

# After purge count remaining points inside loop
answer = 0
for row in expanded_map:
    for point in row:
        if point == "x": answer += 1

print("Part 2 Answer: ", answer)
