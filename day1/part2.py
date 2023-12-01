# Use a dictionary to store the words representing each of the digits, 1-9
# Substitute the correpsonding digit in the place of the word in the original string
# Use your method from part 1 to process the new string

import re

# Map all of the words corresponding to the digits, 1-9, in a dict
num_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def word_to_digit(input_string, num_map):

    # Use the hash map to replace the word with the digit
    for word, digit in num_map.items():
        input_string = input_string.replace(word, digit)
    return input_string


def convert_words_left_to_right(input_string):
    
    constructed_string = ""

    # Check for words as you build the string from left to right, then do the conversion
    for char in input_string:
        constructed_string += char
        constructed_string = word_to_digit(constructed_string, num_map)
    return constructed_string


def find_last_num(input_string):

    rev_partial_string = ""
    
    # Look through string in reverse order to find the last number as a word
    for char in input_string[::-1]:
        rev_partial_string += char
        end_of_string = word_to_digit(rev_partial_string[::-1], num_map)
        digit_match = re.search(r'\d+', end_of_string)

        # Return the first digit (word or number) that is detected
        if char in num_map.values() or (digit_match and digit_match.group() in num_map.values()):
            return char if char in num_map.values() else digit_match.group()
    return None



# Specify the path to your text file
file_path = 'input.txt'

# Initialise a variable to store the total
total = 0

# Open the file in read mode and iterate through each line
with open(file_path, 'r') as file:

    for line in file:
        line_L2R = convert_words_left_to_right(line)

        first_num = re.search(r'\d+', line_L2R)
        first_num = int(first_num.group()[0])
        last_num = find_last_num(line)

        digit_list = [str(first_num), str(last_num)]
        current_num = ''.join(digit_list)

        total += int(current_num)

print(total)