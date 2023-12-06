# Need to keep track of the location of each symbol and scan the surrounding 3 x 3 area for numbers
# Might also need to get the numbers from each line and store in a list
# The numbers that aren't detected by a symbol after the scan can be removed from the list
# Remaining numbers from the list can be summed -> do this for each row
# Symbols: @, #, $, %, &, *, -, +, =, / (10 in total)

# Based on the input data, assume no symbols will be present on any of the edges / borders

# Matrix coordinates to scan would be as follows:
# (r-1, c-1), (r-1, c), (r-1, c+1) ...
# (r, c-1),   (r, c),   (r, c+1)   ...
# (r+1, c-1), (r+1, c), (r+1, c+1) ...
# ...

# Use pandas to organise input data into a matrix, use size function to determine rows and cols in input data
# For a given coordinate (r, c), scan through using these two nested for loops:
# for r in range(1, rows-1):
    # for c in range(1, cols-1):
        # if matrix[r][c] in symbols:
            # Scan 3 x 3 area to see if there are any numbers (MAKE SURE TO AVOID DOUBLE COUNTING)

import pandas as pd

symbols = {'@', '#', '$', '%', '&', '*', '-', '+', '=', '/'}

def extract_digits(string, position):
    # Check if the given position is within the bounds of the string
    if position < 0 or position >= len(string):
        return "Position out of bounds"

    # Initialize variables to store the result
    result = ""
    
    # Iterate left from the given position
    for i in range(position, -1, -1):
        # If the character is a digit, add it to the result
        if string[i].isdigit():
            result = string[i] + result
        # If the character is a dot, stop iterating
        elif string[i] == '.':
            break
        # If the character is not a digit or dot, stop iterating
        else:
            break
    
    # Iterate right from the given position
    for i in range(position + 1, len(string)):
        # If the character is a digit, add it to the result
        if string[i].isdigit():
            result += string[i]
        # If the character is a dot, stop iterating
        elif string[i] == '.':
            break
        # If the character is not a digit or dot, stop iterating
        else:
            break
    return int(result)


def make_df(input_data_file_path):

    # Read the content of the file
    with open(input_data_file_path, 'r') as file:
        input_data = file.read()
        lines = input_data.split('\n')

        # Create a list of lists representing the matrix
        matrix = [list(line) for line in lines]

        # Create a DataFrame from the matrix
        df = pd.DataFrame(matrix)
        return df



# Create df from input data
data = make_df('input.txt')
data_copy = data.copy()
rows, cols = data.shape
print(data)

# Initialise a list of numbers to keep (which need to be summed up later)
nums_list = []

# Begin looping through elements starting from (1, 1) and ending at (r-1, c-1)
for r in range(1, rows-1):
    for c in range(1, cols-1):
        if data.iloc[r, c] in symbols:

            # Scan 3 x 3 area
            for i in range(r - 1, r + 2):
                
                # Store non-duplicate numbers during a 3 x 3 scan before adding to the ordered_list
                # Reset after each iteration of the loop
                seen = set()

                for j in range(c - 1, c + 2):

                    # Find which numbers to keep
                    if str(data.iloc[i, j]).isdigit():
                        string = ''.join(map(str, data.iloc[i, :]))
                        position = j
                        seen.add(int(extract_digits(string, position)))
                        # print(string)
                        # print(seen)

                        # Check to see if scan has worked
                        data_copy.iloc[i, j] = 0

                    # Skip the current position (r, c)
                    if i == r and j == c:
                        continue
                    
                    # Process or scan the position (i, j)
                    # print(f"Scanning position: ({i}, {j})")

                # Extract relevant numbers from each line of the input file and store in a list
                # If a certain number has been seen, add it to the list
                element = int(extract_digits(string, position))
                if element in seen:
                    nums_list.append(element)

print(nums_list)
print(sum(nums_list))

# Export data_copy to a .txt file
export_file_path = 'check_output.txt'
data_copy.to_csv(export_file_path, sep=' ', index=False, header=False)