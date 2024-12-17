# Q.10 count the frequency of the element in the list ?

from recursiveFuncModule import frequency_count,frequency_count_recursive,global_dictionary
# Input list of elements
input_list = [int(x) for x in input("\n Enter elements of the list (separated by spaces): ").split()]
# Dictionary to store frequency count of each element
frequency = global_dictionary
# Loop through each element in the list and count the occurrences
for element in input_list:
    if element in frequency:
        frequency[element] += 1  
        # If element already in dictionary, increment its count
    else:
        frequency[element] = 1  
        # If element is not in dictionary, set its count to 1
        
# Using Manual loop method
print("\nFrequency of each element in {key : -> value} pair :")
for element, count in frequency.items():
    print(f"Key : [{element}] -> Value : [{count}]")
    
# Using the iterative function
print("\nFrequency of each element (Iterative) in {key : -> value} pair:")
frequency = frequency_count(input_list)
for element, count in frequency.items():
    print(f"Key : [{element}] -> Value : [{count}]")
    
# Using the recursive function
print("\nFrequency of each element (Recursive) in {key : -> value} pair:")
frequency_recursive = frequency_count_recursive(input_list)
for element, count in frequency_recursive.items():
    print(f"Key : [{element}] -> Value : [{count}]")
