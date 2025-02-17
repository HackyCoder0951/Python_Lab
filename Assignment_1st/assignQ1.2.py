# Q.2 Count frequency of positive, negative and zero numbers in a given list of numbers?

from recursiveFuncModule import get_user_input, count_numbers, count_numbers_recursive
# Get user input for the list of numbers
num_list = get_user_input()
# Optional additional method using a loop
print("\nCounting numbers using a manual loop :")
positives = 0
negatives = 0
zeroes = 0
# Loop through the numbers and count positives, negatives, and zeroes
for num in num_list:
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
    else:
        zeroes += 1
# Display the list to the user
print("\nEntered List Elements :", num_list)
print(f"Positives : {positives}, Negatives : {negatives}, Zeroes : {zeroes}")
# Count numbers using the iterative function
print("\nCounting numbers using the iterative function :")
positives, negatives, zeros = count_numbers(num_list)
print(f"Positives : {positives}, Negatives : {negatives}, Zeroes : {zeros}")
# Count numbers using the recursive function
print("\nCounting numbers using the recursive function :")
positives, negatives, zeros = count_numbers_recursive(num_list)
print(f"Positives : {positives}, Negatives : {negatives}, Zeroes : {zeros}","\n")

# the f in print is f-string formatting ( formatted string literal )
# And f-string allows you to embeded expressions inside string literals,
# using curly braces {} to directly insert variables or expressions into a string