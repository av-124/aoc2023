# Find number of common elements in each set
# If there is a match, points per card = 2 ^ (matches - 1)
# No match = 0 points

def points_per_card(input_data):
        
    # Data cleaning
    numbers = input_data.split(': ')[1]
    numbers = numbers.replace('  ', ' ')    # replace double spaces with a single space
    winning_nums = numbers.split(' | ')[0]
    your_nums = numbers.split(' | ')[1]

    winning_set = set(winning_nums.strip().split(' '))
    your_set = set(your_nums.strip().split(' '))
    print(winning_set & your_set)

    no_of_matches = int(len(winning_set & your_set))
    print(no_of_matches)

    if no_of_matches > 0:
        points = 2 ** (no_of_matches - 1)
    else:
        points = 0
    return points


# Specify the path to your text file
file_path = 'input.txt'

# Open the file in read mode and iterate through each line
with open(file_path, 'r') as file:
    total = 0
    i = 0

    for line in file:
        total += points_per_card(line)
        print('Cards counted so far = ' + str(i))
        print('Total sum so far = ' + str(total) + '\n')
        i += 1