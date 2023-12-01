# Define a function that reads in .txt file line by line
# Find the first integer and the last integer in the string, then concatenate

import re

def find_and_concat_digits(input_string):

    # Use regular expression to extract integers
    first_num = re.search(r'\d+', input_string)
    last_num = re.search(r'\d+', input_string[::-1])

    # Group the first and the last digit in a list, then concatenate
    digit_list = [first_num.group()[0], last_num.group()[0]]
    concat_digits = ''.join(digit_list)
    return concat_digits



# # Specify the path to your text file
# file_path = 'input.txt'

# # Open the file in read mode and iterate through each line
# with open(file_path, 'r') as file:
    
#     # Initialise a variable to store the total
#     total = 0
    
#     for line in file:
#         current_num = find_and_concat_digits(line)
#         total += int(current_num)

# print(total)