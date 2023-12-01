#!/usr/bin/python3
# Day 1 Puzzle

#-----------------------------------------------------
#Read Input
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
    for item in line:                           # Find First digit
        if item.isnumeric(): 
            first_digit = item
            break
    for item in reversed(line):                 # Find Last digit
        if item.isnumeric(): 
            last_digit = item
            break
    answer += int(first_digit+last_digit)       # combine as strings and sum to answer after combined
print("Part 1 Answer:", answer)
#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
answer = 0
num_reference = [("one", 1), ("two",2), ("three",3), ("four",4), ("five",5), ("six",6), ("seven",7), ("eight",8),("nine",9)]

for line in lines:
    first_digit_index = 999
    last_digit_index = -1
    temp = line
    for num in num_reference:                                           # For each possible written digit find the first and last instance within each input line
        first_instance = line.find(num[0])                              # Index of First Instance of number (-1 if not found)
        last_instance = line.rfind(num[0])                              # Index of Last instance of number (-1 if not found)

        if first_instance < first_digit_index and first_instance != -1: # Note index and value of the first and last numbers found within the input string
            first_digit_index = first_instance
            first_digit = str(num[1])
        if last_instance > last_digit_index:
            last_digit_index = last_instance
            last_digit = str(num[1])

    for i,item in enumerate(line):                                      # Check for first found numeric value in input string
        if item.isnumeric():                                            # If index of numeric number preceeds index of first word, override first digit value
            if i < first_digit_index: first_digit = item
            break
    for i,item in enumerate(reversed(line)):                            # Check for last found numeric value in input string
        if item.isnumeric():                                            # If index of numeric number is larger than index of last word, override last digit value
           if len(line) - 1 - i > last_digit_index: last_digit = item
           break
    #print(first_digit,last_digit)
        
    answer += int(first_digit+last_digit)
print("Part 2 Answer:" ,answer)


