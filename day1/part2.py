# Use a dictionary to store the words representing each of the digits, 1-9
# Substitute the correpsonding digit in the place of the word in the original string
# Use your method from part 1 to process the new string

import part1

def word_to_digit(input_string):
    
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

    # Use the hash map to replace the word with the digit
    for word, digit in num_map.items():
        input_string = input_string.replace(word, digit)
    return input_string


def convert_words_left_to_right(input_string):
    
    constructed_string = ""

    # Check for words as you build the string from left to right, then do the conversion
    for char in input_string:
        constructed_string += char
        constructed_string = word_to_digit(constructed_string)
    return constructed_string



# Specify the path to your text file
file_path = 'input.txt'

# Initialise a variable to store the total
total = 0

# Open the file in read mode and iterate through each line
with open(file_path, 'r') as file:
    
    for line in file:
        line_final = convert_words_left_to_right(line)
        current_num = part1.find_and_concat_digits(line_final)
        total += int(current_num)

print(total)