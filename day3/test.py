import pandas as pd

symbols = {'@', '#', '$', '%', '&', '*', '-', '+', '=', '/'}

def extract_digits(string, position):
    if position < 0 or position >= len(string):
        return 0

    result = ""
    
    for i in range(position, -1, -1):
        if string[i].isdigit():
            result = string[i] + result
        elif string[i] == '.':
            break
        else:
            break
    
    for i in range(position + 1, len(string)):
        if string[i].isdigit():
            result += string[i]
        elif string[i] == '.':
            break
        else:
            break
    
    return int(result) if result else 0

def make_df(input_data_file_path):
    with open(input_data_file_path, 'r') as file:
        input_data = file.read()
        lines = input_data.split('\n')

        matrix = [list(line) for line in lines]
        df = pd.DataFrame(matrix)
        return df

data = make_df('input.txt')
data_copy = data.copy()
rows, cols = data.shape

nums_list = []

for r in range(1, rows-1):
    for c in range(1, cols-1):
        if data.iloc[r, c] in symbols:
            seen = set()
            string = ''.join(map(str, data.iloc[r, :]))

            print(f"Symbol: {data.iloc[r, c]}")
            
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    print(f"Position: ({i}, {j}), Value: {data.iloc[i, j]}")
                    
                    if str(data.iloc[i, j]).isdigit():
                        position = j
                        seen.add(extract_digits(string, position))

            print(f"Seen set: {seen}")
            
            element = extract_digits(string, position)
            if element in seen:
                nums_list.append(element)

print(nums_list)
print(sum(nums_list))
