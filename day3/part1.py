# Need to keep track of the location of each symbol and scan the surrounding 3 x 3 area for numbers
# Need to decide how many rows of the input to scan each time – this will depend on the number of rows in total
# Might also need to strip out all of the numbers from each line and store in a list

# Alternative approach: Cycle through each digit in the number and scan 3 x 3 area for symbol
# The numbers that don't detect a symbol after the scan can be removed from the list
# Remaining numbers from the list can be summed -> do this for each row
# Symbols: @, #, $, %, &, *, -, +, =, / (10 in total)

# Matrix coordinates would be as follows:
# (0, 0), (0, 1), (0, 2) ...
# (1, 0), (1, 1), (1, 2) ...
# (2, 0), (2, 1), (2, 2) ...
# ...

# Ignoring the rows 0 & n and cols 0 & n, the scan area can be expressed as this general solution:

# scan_coords = [-1, 0, 1]

# Use pandas to organise into a matrix, use size function to determine rows and cols in input data
# for a given coordinate (r, c), scan through using these two nested for loops:
# for r in range(1, rows-1):
    # for c in range(1, cols-1):

import re
import pandas

symbols = {'@', '#', '$', '%', '&', '*', '-', '+', '=', '/'}



# Specify the path to your text file
file_path = 'input.txt'

# Open the file in read mode and iterate through each line
with open(file_path, 'r') as file:
    
    for line in file:
        
        nums_to_keep = re.findall(r'\d+', line)

        for i in range(0, len(line)):
            if line[i] in symbols:
                print(len(line))