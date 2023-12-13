#!/usr/bin/python3
# Day 13 Puzzle

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
# Prints grid with indicators highlighting verticle mirror
def print_vert(grid, split_it):
    indicator = ' ' * (split_it-1)
    indicator += "!!"

    remaining_space = len(grid[0]) - len(indicator)
    indicator += (' ' * remaining_space)

    print(indicator)
    for row in grid:
        print(row)

# Prints grid with indicators highlighting horizontal mirror
def print_hor(grid, split_it):
    temp = grid.copy()
    temp[split_it-1] += '<'
    temp[split_it] += '<'

    for line in temp:
        print(line)

# Finds vertical split for part 1
def find_vertical(grid):
    it = 1

    while it < len(grid[0]):
        mirrored = True
        for row in grid:
            seg1 = row[:it]
            seg2 = row[it:]

            if len(seg1) >= len(seg2):
                big = seg1[::-1]
                small = seg2
            else:
                big = seg2
                small = seg1[::-1]

            if not big.startswith(small):
                mirrored = False
                break
        
        if mirrored:
            print_vert(grid, it)
            return it
        else: it += 1
    
    return 0

# Finds horizontal split for part 1
def find_horizontal(grid):
    it = 1

    while it < len(grid):
        seg1 = grid[:it]
        seg2 = grid[it:]

        if len(seg1) >= len(seg2):
                big = list(reversed(seg1))
                small = seg2
        else:
            big = seg2
            small = list(reversed(seg1))

        mirrored = True
        for i, line in enumerate(small):
            if line != big[i]:
                mirrored = False
                break
        
        if mirrored:
            print_hor(grid, it) 
            return it * 100
        else: it += 1

    return 0

# Finds vertical split for part 2
def smudged_vertical(grid):
    it = 1
    smudge_counter = 0

    while it < len(grid[0]):
        mirrored = True
        for row in grid:
            seg1 = row[:it]
            seg2 = row[it:]

            if len(seg1) >= len(seg2):
                big = list(seg1[::-1])
                small = list(seg2)
            else:
                big = list(seg2)
                small = list(seg1[::-1])

            if big[:len(small)] != small:
                for x, point in enumerate(small):
                    if point != big[x]: 
                            smudge_counter += 1

                    if smudge_counter > 1:
                        mirrored = False
                        smudge_counter = 0
                        break
            if not mirrored: break
        
        if mirrored and smudge_counter == 1:
            print_vert(grid, it) 
            return it
        else: it += 1
    
    return 0

# Finds horizontal split for part 2
def smudged_horizontal(grid):
    it = 1
    smudge_counter = 0

    while it < len(grid):
        seg1 = grid[:it]
        seg2 = grid[it:]

        if len(seg1) >= len(seg2):
                big = list(reversed(seg1))
                small = seg2
        else:
            big = seg2
            small = list(reversed(seg1))

        mirrored = True
        for i, line in enumerate(small):
            if line != big[i]:
                for x, point in enumerate(line):
                    if point != big[i][x]: 
                        smudge_counter += 1

                    if smudge_counter > 1:
                        mirrored = False
                        smudge_counter = 0
                        break

                if not mirrored: break
        
        if mirrored and smudge_counter == 1:
            print_hor(grid, it) 
            return it * 100
        else: 
            it += 1

    return 0
#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
all_grids = []
grid = []

for line in lines:
    if not line:
        all_grids.append(grid)
        grid = []
    
    else: grid.append(line)
all_grids.append(grid)


answer = 0
for grid in all_grids:
    answer += find_horizontal(grid)
    answer += find_vertical(grid)
    print("--------------")        

print(answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
answer = 0
for grid in all_grids:
    answer += smudged_horizontal(grid)
    answer += smudged_vertical(grid)
    print("--------------")        

print(answer)