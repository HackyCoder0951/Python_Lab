def frequency_count_recursive(numbers, frequency=None):
    global global_dictinary
    global_dictinary.clear()
    if frequency is None:
        frequency = {}   
    if not numbers:  # Base case: if the list is empty, return the frequency dictionary
        global_dictinary = frequency
        return frequency  
    # Get the first element in the list
    element = numbers[0]    
    # Update the frequency dictionary
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1
    # Recurse with the rest of the list
    return frequency_count_recursive(numbers[1:], frequency)

def frequency_count(numbers):
    global global_dictinary
    global_dictinary.clear()
    for element in numbers:
        if element in global_dictinary:
            global_dictinary[element] += 1
        else:
            global_dictinary[element] = 1
    return global_dictinary

def get_user_input_dict():
    global global_dictinary
    global_dictinary.clear()
    print("Enter key-value pairs to add to the dictionary. Type 'd' to finish.")
    while True:
        user_input = input("Enter key (or 'd' to finish): ").strip().lower()
        if user_input == 'd':
            break
        key = user_input
        value = input(f"Enter value for key '{key}': ").strip()
        global_dictinary[key] = value
    return global_dictinary

# Input list of elements
input_list = [int(x) for x in input("\n Enter elements of the list (separated by spaces): ").split()]
# Dictionary to store frequency count of each element
frequency = {}
# Loop through each element in the list and count the occurrences
for element in input_list:
    if element in frequency:
        frequency[element] += 1  
        # If element already in dictionary, increment its count
    else:
        frequency[element] = 1  
        # If element is not in dictionary, set its count to 1
# Display the frequency of each element
print("\nFrequency of each element :")
for element, count in frequency.items():
    print(f"Element : {element} -> {count}")
# Using the iterative function
print("\nFrequency of each element (Iterative):")
frequency = frequency_count(input_list)
for element, count in frequency.items():
    print(f"Element : {element} -> {count}")
# Using the recursive function
print("\nFrequency of each element (Recursive):")
frequency_recursive = frequency_count_recursive(input_list)
for element, count in frequency_recursive.items():
    print(f"Element : {element} -> {count}")

if __name__ == "__main__":
    user_dict = get_user_input_dict()
    values = list(user_dict.values())
    print("\nCounting frequencies using iteration:")
    frequency_result_iterative = frequency_count(values)
    print(frequency_result_iterative)
    print("\nCounting frequencies using recursion:")
    frequency_result_recursive = frequency_count_recursive(values)
    print(frequency_result_recursive)
