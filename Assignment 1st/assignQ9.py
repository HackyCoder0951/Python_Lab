# Q.9 find maximum of the three numbers ?

from recursiveFuncModule import get_user_input, max_of_three
    
# Initialize the numbers list using the get_user_input function
numbers = get_user_input()
# numbers = []
# Ensure that the list has at least 'nums' elements

# Initialize the first number as the maximum
three_max_value = numbers[0]

# Loop through the list to find the maximum number manually
for num in numbers:
    if num > three_max_value:
        three_max_value = num

# Display the manually calculated maximum value
print(f"The maximum value is: {three_max_value}")

# Now use the max_of_three function to find the maximum of the first three numbers (if there are at least 3 numbers)
if len(numbers) >= 3:
    three_max_value = max_of_three(numbers[0], numbers[1], numbers[2])
    print(f"The maximum of the three numbers {numbers[0]}, {numbers[1]}, and {numbers[2]} is: {three_max_value}")
else:
    print("There are fewer than 3 numbers, so max_of_three cannot be used.")
