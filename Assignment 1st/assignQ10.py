# Q.10 count the frequency of the element in the list ?

# Input list of elements
input_list = [
    int(x) for x in input("\n Enter elements of the list (separated by spaces): ").split()]

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
print("\nFrequency of each element:")
for element, count in frequency.items():
    print(f"{element}: {count}")

