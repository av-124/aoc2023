# Need to keep track of the location of each symbol and scan the surrounding 3 x 3 area for numbers
# Need to decide how many rows of the input to scan each time – this will depend on the number of rows in total
# Might also need to strip out all of the numbers from each line and store in a list

# Alternative approach: Cycle through each digit in the number and scan 3 x 3 area for symbol
# The numbers that don't detect a symbol after the scan can be removed from the list
# Remaining numbers from the list can be summed -> do this for each row
# Symbols = @, #, $, %, &, *, -, +, =, / (10 in total)

