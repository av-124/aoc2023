# Ignore previous game rule and find the min number of r, g, and b cubes to make each game possible
# Return power (r * g * b)

def get_power_from_game(input_data):

    # Initialise variables
    colour_map = {}
    colours = ['red', 'green', 'blue']
    cube_reveals = []

    # Data cleaning
    input_data = input_data.replace(',', '')
    after_colon = input_data.split(': ')[1]

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

    # print(colour_map)
    
    min_r = max(colour_map['r'])
    min_g = max(colour_map['g'])
    min_b = max(colour_map['b'])
    power = min_r * min_g * min_b
    # print(min_r)
    # print(min_g)
    # print(min_b)
    # print(power)
    return power



# Specify the path to your text file
file_path = 'input.txt'

# Open the file in read mode and iterate through each line
with open(file_path, 'r') as file:
    
    # Initialise a total
    total = 0
    i = 1

    for line in file:
        total += get_power_from_game(line)
        print('Games analysed so far = ' + str(i))
        print('Power sum so far = ' + str(total) + '\n')
        i += 1