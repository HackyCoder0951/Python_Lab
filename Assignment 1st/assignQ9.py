# Q.9 find maximum of the three numbers ?

# Ask the user how many numbers they want to enter
nums = int(input("How many numbers do you want to input? "))

# Initialize an empty list to store the numbers
numbers = []

# Input multiple numbers using a loop
for i in range(nums):
    # getting values inputs in num variable
    num = int(input(f"Enter number {i+1}: "))
    # Adding Values to List using append() method
    numbers.append(num)

# Initialize the first number as the maximum
max_value = numbers[0]

# Loop through the list to find the maximum number
for num in numbers:
    if num > max_value:
        max_value = num

# Display the maximum value
print(f"The maximum value is: {max_value}")
