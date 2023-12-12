#!/usr/bin/python3
# Day 12 Puzzle

#-----------------------------------------------------
# Read Input
#-----------------------------------------------------
#input_file = "input.txt"
input_file = "test.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    #print(lines)
#-----------------------------------------------------
# Function
#-----------------------------------------------------
def make_ints(list):
    new_list = []
    for item in list:
        new_list.append(int(item))

    return new_list

def makes_sense(sequence, target):
    spring_it = 0
    for t in target:
        spring_count = 0
        start_counting = False
        for it, spring in enumerate(sequence[spring_it:]):
            if start_counting == False and spring == '#':
                start_counting = True

            if start_counting and spring == '#': spring_count += 1
            elif start_counting and spring == '.': 
                spring_it = it
                break

        if spring_count != t: return False
    
    return True

def test_options(sequence, targets, rest_of_sequence):
    option_count = 0
    first_unkown = 0
    unmet_targets = targets.copy()
    good_count = 0
    unchecked_start = 0
    hash_group = False

    for i, spring in enumerate(sequence):

        if spring == '#':
            hash_group = True
            good_count += 1

            if good_count > unmet_targets[0]: return option_count

        elif spring == '.' and hash_group:
            if good_count == unmet_targets[0]: #and makes_sense(spring[unchecked_start:i+1], [unmet_targets[0]]):
                good_count = 0
                unchecked_start = i + 1
                unmet_targets.pop(0)
                hash_group = False

                if not unmet_targets and '#' not in sequence[i+1:]:
                    #print(rest_of_sequence + sequence)      # Debug
                    return option_count + 1
                elif not unmet_targets: return option_count

            else: return option_count
                
        elif spring == '?':
            first_unkown = i
            option = sequence.copy()

            option[i] = '#'
            ros = rest_of_sequence + option[:unchecked_start]
            option_count += test_options(option[unchecked_start:], unmet_targets, ros)

            option[i] = '.'
            ros = rest_of_sequence + option[:unchecked_start]
            option_count += test_options(option[unchecked_start:], unmet_targets, ros)
            return option_count

    
    if len(unmet_targets) > 1 or (unmet_targets and good_count != unmet_targets[0]): return option_count
    else:
        #print(rest_of_sequence + sequence)      # Debug
        return option_count + 1

    
#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
answer = 0
for line in lines:
    spring, target = line.split(" ")
    spring = list(spring)
    target = target.split(',')
    target = make_ints(target)

    #print("--------------")
    #print(spring, "****", target)

    answer += test_options(spring, target,[])
    debug = 0

print("Part 1 Answer: ", answer)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
answer = 0
for i, line in enumerate(lines):
    spring, target = line.split(" ")
    spring = list(spring)
    spring.append('?')
    spring = spring.copy() * 5
    spring.pop()

    target = target.split(',')
    target = make_ints(target)
    target = target.copy() * 5

    #print("--------------")
    #print(spring, "****", target)

    answer += test_options(spring, target,[])


print("Part 2 Answer: ", answer)