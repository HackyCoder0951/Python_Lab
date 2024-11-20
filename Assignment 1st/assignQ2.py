# creating list
num_list = [1,2,4.5,-5,-67,8,0,0.0,-4.4,5,-3.3]
# initializing variables
positives = 0
negatives = 0
zeroes = 0

# counting positives,negatives and zeroes 
for num in num_list:
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
    else:
        zeroes += 1
print(f"Positives:{positives},Negatives:{negatives},Zeroes:{zeroes}")

# the f in print is f-string formatting ( formatted string literal )
# And f-string allows you to embeded expressions inside string literals,
# using curly braces {} to directly insert variables or expressions into a string
