#!/usr/bin/python3
# Day 8 Puzzle
#-----------------------------------------------------
# Imports
#-----------------------------------------------------
import math
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
instructions = lines[0]
nodes = {}

for line in lines[2:]:
    node, lr = line.split(" = ")
    nodes[node] = lr[1:-1].split(", ")

current_node = 'AAA'
step_counter = 0

while current_node != "ZZZ":
    for move in instructions:
        step_counter += 1
        if move == 'L': current_node = nodes[current_node][0]
        else: current_node = nodes[current_node][1]

        if current_node == "ZZZ":
            print("Part 1 Answer: ", step_counter)
            break

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
target_nodes = {}       # Dictionary will hold all Z Node Values as keys and the interval they repeat in as values
start_nodes = []        # list holds list of all A nodes to use as start point

# Find all 'A' nodes
for node in list(nodes.keys()):
    if node[-1] == 'A': start_nodes.append(node)

# For each 'A' node, find the 'Z' node it hits and how often that 'Z' node re-appears
for node in start_nodes:
    repeat_int = 0      # Only starts counting once the 'Z' node shows up for first time
    step_counter = 0
    current_node = node
    found_at = 0        # Records at what step the 'Z' node appeared for the first time
    found = False       # indicates if 'Z' node has appeared in pattern yet
    cycled = False      # indicates that 'Z' node has reappeared and pattern is repeating

    # Keep stepping until 'Z' node appears twice
    while not cycled:
        for move in instructions:
            step_counter += 1

            # find next node
            if move == 'L': current_node = nodes[current_node][0]
            else: current_node = nodes[current_node][1]

            if current_node[-1] == 'Z' and found:                       # If second time 'Z' node is seen
                target_nodes[current_node] = step_counter - found_at
                cycled = True
                break
            elif current_node[-1] == 'Z':                               # If first time 'Z' node is seen
                found_at = step_counter
                found = True

# Find least common multiple of all the 'Z' node intervals
# This will be the first step where all 'Z' nodes appear simultaneously
answer = 1
for node in target_nodes:
    answer = math.lcm(answer,target_nodes[node])
    #print(f"{node} --> {target_nodes[node]}")          # Debug. Prints all termination points and their known interval

print("Part 2 Answer: ", answer)
