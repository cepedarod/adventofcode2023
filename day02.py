#!/usr/bin/python3
# Day 2 Puzzle

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
max_red_cubes = 12      # Number of cubes of each color stipulated by puzzle
max_green_cubes = 13
max__blue_cubes = 14
answer = 0
impossible = False

#Look at each game
for line in lines:
    game_id, game_info = line.split(": ")
    game_id = int(game_id.split(" ")[1])

    #look at each hadnfull of cubes
    for draw in game_info.split("; "):
        #Look at the the quantity of each color cubes 
        for color in draw.split(", "):
            quantity, rgb = color.split(" ")
            if rgb == "red" and int(quantity) > max_red_cubes:
                impossible = True
                break
            if rgb == "green" and int(quantity) > max_green_cubes:
                impossible = True
                break
            if rgb == "blue" and int(quantity) > max__blue_cubes:
                impossible = True
                break
        if impossible: break                # If any of the colors exceed the total of cubes of the same color, go to next game 
    if impossible: impossible = False       # Reset Impossible flag for next game
    else: answer += game_id
    
print("Part 1 Answer: ", answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------

answer = 0
impossible = False

for line in lines:
    max_red_cubes = 0           # Larges quantity of each color cube per game
    max_green_cubes = 0
    max__blue_cubes = 0

    game_id, game_info = line.split(": ")
    game_id = int(game_id.split(" ")[1])

    for draw in game_info.split("; "):                                  # Determine larges number of cubes of each color seen in per game
        for color in draw.split(", "):
            quantity, rgb = color.split(" ")

            if rgb == "red" and int(quantity) > max_red_cubes:
                max_red_cubes = int(quantity)
            if rgb == "green" and int(quantity) > max_green_cubes:
                max_green_cubes = int(quantity)
            if rgb == "blue" and int(quantity) > max__blue_cubes:
                 max__blue_cubes = int(quantity)
    game_power = max_red_cubes * max__blue_cubes * max_green_cubes
    answer += game_power
    
print("Part 2 Answer: ", answer)