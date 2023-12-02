# Need to determine if a game is possible where r = 12, g = 13, b = 14
# Input data looks like this:
# Game 15: 7 green, 1 blue; 1 red, 2 green, 1 blue; 7 green
# Make it into a hash map, structured like so:
# my_dict = {
# 'r': [0, 1, 0],
# 'g': [7, 2, 7],
# 'b': [1, 1, 0]
# }
# Check if any elements in each of the lists are larger than r = 12, g = 13, b = 14
# Exclude game if so, return game number if not

def get_valid_game_number(input_data):

    game_rule = {'r': 12,
                'g': 13,
                'b': 14
                }

    # Initialise variables
    colour_map = {}
    colours = ['red', 'green', 'blue']
    cube_reveals = []

    # Data cleaning
    input_data = input_data.replace(',', '')
    before_colon = input_data.split(': ')[0]
    after_colon = input_data.split(': ')[1]

    # Store the game number
    before_colon = before_colon.strip().split(' ')
    game = int(before_colon[before_colon.index('Game')+1])

    # Store all of the cube reveals in a list
    for part in after_colon.split(';'):
        cube_reveals.append(part.strip().split(' '))

    # Initialise an empty list to store the colour count for each reveal in a hash map
    for colour in colours:
        colour_map[colour[0]] = []

    # Update hash map
    for revealed_set in cube_reveals:
        for colour in colours:
            if colour in revealed_set:
                index = revealed_set.index(colour)
                cube_count = int(revealed_set[index - 1])
                colour_map[colour[0]].append(cube_count)
            else:
                colour_map[colour[0]].append(0)

    print(colour_map)
            
    # Initialise a variable to determine if a game should be included or not
    include_game = True

    for key in colour_map.keys():
        for element in colour_map[key]:
            if element > game_rule[key]:
                include_game = False
                print(f"For colour = {key}, {element} breaks the game rule.")
                print("Exclude game.")
                return 0
   
    if include_game == True:
        print(f"Include game {game}.")
        return game



# Specify the path to your text file
file_path = 'input.txt'

# Open the file in read mode and iterate through each line
with open(file_path, 'r') as file:
    
    # Initialise a total
    total = 0
    i = 1

    for line in file:
        total += get_valid_game_number(line)
        print('Games analysed so far = ' + str(i))
        print('Total sum so far = ' + str(total) + '\n')
        i += 1