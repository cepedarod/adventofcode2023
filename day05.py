#!/usr/bin/python3
# Day 5 Puzzle

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
def convert(dest_min, src_min, number):
    diff = number - src_min
    return dest_min + diff

def print_almanac(almanac):
    for i, chapter in enumerate(almanac):
        print(f"------- Step: {i} -------")
        for entrie in chapter:
            print(f"{entrie.start} - {entrie.end} | {entrie.value_modifier}") 

class range_segment():
    def __init__(self, rng_start, rng_end, value_modifier):
        self.start = rng_start + value_modifier
        self.end = rng_end + value_modifier
        self.sub_ranges = []
        self.value_modifier = value_modifier
        self.range_bottom = 99999999999

    def __lt__(self, other):
        return self.start < other.start
    
    def print_best_branch(self):
        print(f"RANGE: ({self.start} - {self.end}), Mod: {self.value_modifier}")
        if self.sub_ranges:
            best_path_index = 0
            lowest_point = 99999999999
            for i,segment in enumerate(self.sub_ranges):
                if segment.range_bottom < lowest_point:
                    lowest_point = segment.range_bottom
                    best_path_index = i
            self.sub_ranges[best_path_index].print_best_branch()

    def print_single_branch(self):
        print(f"RANGE: ({self.start} - {self.end}), Mod: {self.value_modifier}")
        if self.sub_ranges:
            self.sub_ranges[0].print_single_branch()

    def path_recursion(self, almanac, step_number):
        if self.start == 1568886369:
            debug = 0
        
        if step_number == 7: 
            self.range_bottom = self.start
            return self.start
        
        range_it = self.start

        for range in almanac[step_number]:
            if range_it <= range.end:
                if range_it < range.start:
                    sub_range = range_segment(range_it, range.start - 1, 0)
                    lp = sub_range.path_recursion(almanac, step_number + 1)
                    self.sub_ranges.append(sub_range)
                    range_it = range.start

                    if lp < self.range_bottom: self.range_bottom = lp
                
                if range.end >= self.end:
                    sub_range = range_segment(range_it, self.end, range.value_modifier)
                    lp = sub_range.path_recursion(almanac, step_number + 1)
                    self.sub_ranges.append(sub_range)
                    range_it = self.end + 1

                    if lp < self.range_bottom: self.range_bottom = lp
                    break   #Convert to return

                else:
                    sub_range = range_segment(range_it, range.end, range.value_modifier)
                    lp = sub_range.path_recursion(almanac, step_number + 1)
                    self.sub_ranges.append(sub_range)
                    range_it = range.end + 1

                    if lp < self.range_bottom: self.range_bottom = lp
        
        if range_it < self.end:
            sub_range = range_segment(range_it, self.end, 0)
            lp = sub_range.path_recursion(almanac, step_number + 1)
            self.sub_ranges.append(sub_range)

            if lp < self.range_bottom: self.range_bottom = lp

        return self.range_bottom
        



                

    
    def add_subranges(self, almanac, chapter):
        range_it = self.start
        lowest_point = 99999999999
        winning_seed = 0

        if chapter == 7:
            self.range_bottom = self.start
            return self.range_bottom, self.start - self.value_modifier
        
        for range in almanac[chapter]:
            if range_it < range.start and self.end < range.start:
                new_range = range_segment(range_it, self.end, 0)
                lowest_point, seed_value = new_range.add_subranges(almanac, chapter + 1)
                self.sub_ranges.append(new_range)

                if lowest_point < self.range_bottom: 
                    self.range_bottom = lowest_point
                    winning_seed = seed_value
                break
                
            elif range_it < range.start:
                new_range = range_segment(range_it, range.start, 0)
                lowest_point, seed_value = new_range.add_subranges(almanac, chapter + 1)
                self.sub_ranges.append(new_range)

                if lowest_point < self.range_bottom: 
                    self.range_bottom = lowest_point
                    winning_seed = seed_value

                range_it = range.start
            
            if self.end <= range.end:
                new_range = range_segment(range_it, self.end, range.value_modifier)
                lowest_point, seed_value = new_range.add_subranges(almanac, chapter + 1)
                self.sub_ranges.append(new_range)

                if lowest_point < self.range_bottom: 
                    self.range_bottom = lowest_point
                    winning_seed = seed_value
                break
            elif range_it < range.end:
                new_range = range_segment(range_it, range.end, range.value_modifier)
                lowest_point, seed_value = new_range.add_subranges(almanac, chapter + 1)
                self.sub_ranges.append(new_range)

                if lowest_point < self.range_bottom: 
                    self.range_bottom = lowest_point
                    winning_seed = seed_value

                range_it = range.end
                #new_range = range_segment(range.end, self.end, 0)
                #new_range.add_subranges(almanac, chapter + 1)
                #self.sub_ranges.append(new_range)
            
        self.sub_ranges.sort()
        #print("-------")
        #print (self.start, self.end)
        #for r in self.sub_ranges:
            #print(r.start,r.end)
        
        return self.range_bottom, winning_seed - self.value_modifier
        






        
#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
seeds = lines[0].split(": ")[1].split(" ")
almanac = [[],[],[],[],[],[],[]]
section = 0
lowest_location = 99999999999

for line in lines[3:]:
    if line != "" and line[0].isnumeric():
        almanac[section].append(line.split(" "))
    elif line != "": section += 1

for seed in seeds:
    loc = int(seed)
    for chapter in almanac:
        for line in chapter:
            dest_min = int(line[0])
            src_min = int(line[1])
            src_max = src_min + int(line[2]) - 1

            if loc >= src_min and loc <= src_max:
                loc = convert(dest_min, src_min, loc)
                break

    if loc < lowest_location: lowest_location = loc

print("Part 1 Answer: ",lowest_location)

#-----------------------------------------------------
# Part 2
#-----------------------------------------------------
seeds_2 = []
almanac_2 = [[],[],[],[],[],[],[]]
almanac_3 = [[],[],[],[],[],[],[]]
it = 0
while it < len(seeds):
    rng_start = int(seeds[it])
    rng_end = rng_start + int(seeds[it+1]) - 1
    seeds_2.append(range_segment(rng_start, rng_end, 0))
    it+=2
seeds_2.sort()

for i,chapter in enumerate(almanac):
    #print("-------")
    for line in chapter:
        src_min = int(line[1])
        src_max = src_min + int(line[2]) - 1
        modifier = int(line[0]) - src_min
        start_segment = range_segment(src_min, src_max, 0)
        start_segment.value_modifier = modifier
        almanac_2[i].append(start_segment)
        #print("in chapter ", i, "anything between ", src_min , "to", src_max, "will increment by ", modifier,". ", src_min, "->", src_min + modifier)
    almanac_2[i].sort()

    if almanac_2[i][0].start > 0:
        rng_end = almanac_2[i][0].start - 1
        start_segment = range_segment(0, rng_end, 0)
        almanac_2[i].insert(0, start_segment)


for i, chapter in enumerate(almanac_2):
    range_it = 0
    
    for range in chapter:
        if range.start != 0 and range_it == 0 :
            r_start = 0
            rng_end = range.start - 1
            almanac_3[i].append(range_segment(r_start, rng_end, 0))
            range_it = range.start
            print(f"Chapter {i} - added starting section")

        if range_it < range.start:
            r_start = range_it
            rng_end = range.start - 1
            almanac_3[i].append(range_segment(r_start, rng_end, 0))
            range_it = range.start
        else:
            new_range = range_segment(range_it, range.end, 0)
            new_range.value_modifier = range.value_modifier
            almanac_3[i].append(new_range)
            range_it = range.end + 1
    almanac_3[i].sort()
    
#print("-------")
#print("v3")
print_almanac(almanac_2)
print("-------")
print("-------")
print("-------")     
print_almanac(almanac_3)
for i, chapter in enumerate(almanac_2):
    print(f"Chapter {i} - {len(chapter)}")

lowest_location = 99999999999 
for i,seed_range in enumerate(seeds_2):
    loc = seed_range.path_recursion(almanac_2, 0)
    if loc < lowest_location:
        best_range_index = i 
        lowest_location = loc
    #print("-------")
    #seed_range.print_best_branch()

seeds_2[best_range_index].print_best_branch()


print("Answer Part 2: ", lowest_location)

