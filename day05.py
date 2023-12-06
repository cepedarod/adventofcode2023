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
# Used for making conversations for part 1
def convert(dest_min, src_min, number):
    diff = number - src_min
    return dest_min + diff

# Print almanac content for debugging
def print_almanac(almanac):
    for i, chapter in enumerate(almanac):
        print(f"------- Step: {i} -------")
        for entrie in chapter:
            print(f"{entrie.start} - {entrie.end} | {entrie.value_modifier}") 

# Main object for handling part 2
class range_segment():
    # When creating range segment add the value modifier stipulated by the almanac when converting to the next metric
    def __init__(self, rng_start, rng_end, value_modifier):
        self.start = rng_start + value_modifier
        self.end = rng_end + value_modifier
        self.sub_ranges = []                        # Stores all subranges that values in this range could result after the next conversion
        self.value_modifier = value_modifier        # Stores the value modifier applied to this range when being generated
        self.range_bottom = 99999999999             # Stores the lowest known location in its subrange tree

    # Allows the use of the sort() method on this object. Lists of this object are sorted by the start value of the range from lowest to highest
    def __lt__(self, other):
        return self.start < other.start
    
    # Prints subrange chain to highlight the path to lowest known location within this range
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
   
   # Prints first branch of this range all the way to location (Used for Debugging) 
    def print_single_branch(self):
        print(f"RANGE: ({self.start} - {self.end}), Mod: {self.value_modifier}")
        if self.sub_ranges:
            self.sub_ranges[0].print_single_branch()

    # Main function to solve Part 2
    # This function both adds subranges that represent possible conversion values and recursively pulls the lowest found location  of all possible options
    # Function take the full almanac, and reference of what conversion step we are currently on so function can be used recursively
    # Ranges in each section of the almanac are sorted before being passed to here
    def path_recursion(self, almanac, step_number):
        
        # Rock bottom. This If statement is what triggers the recursion to collaps on itself once all 7 conversions have been made
        # Since the lowest value in the final range is its first value, return that first value
        if step_number == 7: 
            self.range_bottom = self.start
            return self.start
        
        range_it = self.start               # Variable used to keep track of what parts of this range have already been accounted for

        for range in almanac[step_number]:  # iterate through each line of current almanac section
            
            if range_it <= range.end:       # only engage with this line if the satrt of this range is less than the end value of the almanac line
                if range_it < range.start:  
                    sub_range = range_segment(range_it, range.start - 1, 0)                 # If the start of this range preceeds the range in almanac
                    lp = sub_range.path_recursion(almanac, step_number + 1)                 # add a subrange with 0 modification from this range start to almanac range start
                    self.sub_ranges.append(sub_range)                                       # When recursive function is called, almanac index (step number) is incremented by 1
                    range_it = range.start      # Move range_it to next point of interest

                    if lp < self.range_bottom: self.range_bottom = lp                       # If lowest point found in this recursion is current lowest, record it as such
                
                if range.end >= self.end:                                                   # If current alamanac line encompases the rest of the range
                    sub_range = range_segment(range_it, self.end, range.value_modifier)     # Create subrange for remainder of this range using stipulated modifier
                    lp = sub_range.path_recursion(almanac, step_number + 1)
                    self.sub_ranges.append(sub_range)
                    range_it = self.end + 1     # Move range_it to next point of interest

                    if lp < self.range_bottom: self.range_bottom = lp                       # If lowest point found in this recursion is current lowest, record it as such
                    break   # Since this range has been accounted for in its entirety, no need to look at more lines

                else:       # If this range extends beyond the almanac range, create subrange up to the almanac limit and wait for next line (in next loop) to process rest
                    sub_range = range_segment(range_it, range.end, range.value_modifier)
                    lp = sub_range.path_recursion(almanac, step_number + 1)
                    self.sub_ranges.append(sub_range)
                    range_it = range.end + 1

                    if lp < self.range_bottom: self.range_bottom = lp                       # If lowest point found in this recursion is current lowest, record it as such
        
        if range_it < self.end:                                                             # If after reading the whole almanac section, there is left overs from this range
            sub_range = range_segment(range_it, self.end, 0)                                # add a subsection for what remains with 0 modifier
            lp = sub_range.path_recursion(almanac, step_number + 1)
            self.sub_ranges.append(sub_range)

            if lp < self.range_bottom: self.range_bottom = lp                               # If lowest point found in this recursion is current lowest, record it as such

        return self.range_bottom                                                            # All recursions completed, return lowest known value
        
#-----------------------------------------------------
# Part 1
#-----------------------------------------------------
seeds = lines[0].split(": ")[1].split(" ")          # List holding starting Seed values
almanac = [[],[],[],[],[],[],[]]                    # 2D list that will hold all almanac info
section = 0                                         # Used for indexing of almanac
lowest_location = 99999999999                       # Used to record Answer

for line in lines[3:]:                              # Initialize Alamanc (Ignore lines with seed info)
    if line != "" and line[0].isnumeric():
        almanac[section].append(line.split(" "))
    elif line != "": section += 1

for seed in seeds:                                  # Solve Puzzle
    loc = int(seed)
    for chapter in almanac:
        for line in chapter:
            dest_min = int(line[0])                 # Extract key parameters from line
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
seeds_2 = []                            # Holds starting points for part 2
almanac_2 = [[],[],[],[],[],[],[]]      # Holds improved version of the almanac for part 2
it = 0
while it < len(seeds):                  # Convert input into a range and staore it using range_Segment object
    rng_start = int(seeds[it])
    rng_end = rng_start + int(seeds[it+1]) - 1
    seeds_2.append(range_segment(rng_start, rng_end, 0))
    it+=2
seeds_2.sort()

for i,chapter in enumerate(almanac):                        # Translate basic almanac from part 1 into robust one using range_segments for each line
    #print("-------")
    for line in chapter:
        src_min = int(line[1])
        src_max = src_min + int(line[2]) - 1
        modifier = int(line[0]) - src_min
        start_segment = range_segment(src_min, src_max, 0)  # Initialize each line with 0 modifier to not distort values as these are for reference
        start_segment.value_modifier = modifier             # add reference modifier so correct change takes place when querring this object
        almanac_2[i].append(start_segment)

    almanac_2[i].sort()                                     # sort all lines in almanac so ranges are in order from lowest to highest

    if almanac_2[i][0].start > 0:                           # make sure that each section of the almanac has its first range starting at 0
        rng_end = almanac_2[i][0].start - 1                 # if not there add the segment with 0 modifier for reference
        start_segment = range_segment(0, rng_end, 0)
        almanac_2[i].insert(0, start_segment)

#print_almanac(almanac_2)       # Debug

lowest_location = 99999999999 
for i,seed_range in enumerate(seeds_2):                 # Find lowest location for each initial seed range
    loc = seed_range.path_recursion(almanac_2, 0)

    if loc < lowest_location:                           # Used for Debug printing
        best_range_index = i 
        lowest_location = loc

#seeds_2[best_range_index].print_best_branch()      # Debug

print("Part 2 Answer: ", lowest_location)

