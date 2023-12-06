#!/usr/bin/python3
# Day 6 Puzzle

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
times = lines[0].split(":")[1].strip()
distances = lines[1].split(":")[1].strip()

times = times.split("     ")
distances = distances.split("   ")
answer = 1
for x, time in enumerate(times):
    winning_options = 0
    p_time = 0

    while p_time < int(time):
        r_time = int(time) - p_time
        dist = r_time * p_time
        if dist > int(distances[x]): winning_options += 1
        p_time += 1
    
    answer = answer * winning_options
print("Part 1 Answer:", answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
total_time = ""
total_distance =  ""
for x, time in enumerate(times):
    total_time += time
    total_distance += distances[x]

total_time = int(total_time)
total_distance = int(total_distance)

answer = 1
winning_options = 0
p_time = 1000000
scroll_speed = 100000

while True:
    r_time = total_time - p_time
    dist = r_time * p_time
    if dist > total_distance and scroll_speed == 1:
        winning_options = int(total_time - (p_time * 2) + 1)
        print("Part 2 Answer:", winning_options)
        exit()
    elif dist > total_distance and scroll_speed < 1000: 
        p_time -= scroll_speed
        scroll_speed = 1
    elif dist > total_distance:
        p_time -= scroll_speed
        scroll_speed = scroll_speed / 10

    p_time += scroll_speed
    


