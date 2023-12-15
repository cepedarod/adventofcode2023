#!/usr/bin/python3
# Day 15 Puzzle

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
def hash(s):
    string_val = 0
    for char in s:
        string_val += ord(char) 
        string_val = string_val * 17
        string_val = string_val % 256
    
    return string_val
#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
strings = lines[0].split(",")

answer = 0

for s in strings:
    string_val = 0
    for char in s:
        string_val += ord(char) 
        string_val = string_val * 17
        string_val = string_val % 256
    answer += string_val

print(answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
boxes = []
for x in range(256): boxes.append([])

for step in strings:
    found = False
    if '=' in step:
        label, lens = step.split("=")
        box_num = hash(label)

        for i, item in enumerate(boxes[box_num]):
            if item[0] == label:
                boxes[box_num][i] = (label, lens)
                found = True
                break
        
        if not found: boxes[box_num].append((label, lens)) 

    elif '-' in step:
        label = step[:-1]
        box_num = hash(label)

        for i, item in enumerate(boxes[box_num]):
            if item[0] == label:
                boxes[box_num].pop(i)
                break

total_foc = 0
for box_it, box in enumerate(boxes):
    for l, lens in enumerate(box):
        foc_power = (box_it+1) * (l+1) * int(lens[1])
        total_foc += foc_power

print(total_foc)

