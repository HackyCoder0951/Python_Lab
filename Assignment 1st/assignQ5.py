# Q.5 even or odd from the list ?

from recursiveFuncModule import get_number_list,separate_even_odd,even_odd_recursive

n = int(input("Enter the total number of element in the list : "))

num_list = [] # number list
even_list = [] # even number list
odd_list = [] # odd number list

for i in range(n):
    value = int(input(f"Enter {i+1} element : "))
    num_list.append(value)  # assigning values into num_list[]

for i in num_list:
    if(i % 2 == 0): # check reminder 
        even_list.append(i) # assigning values into even_list[]
    else:
        odd_list.append(i) # assigning values into odd_list[]

print("List of All Numbers :",num_list)
print("List of Even Numbers :",even_list)
print("List of Odd Numbers :",odd_list)

# Get the number list from the user
num_list = get_number_list(n)

# Use the `separate_even_odd` function
even_list, odd_list = separate_even_odd(num_list)

# Use the `even_odd_recursive` function
even_recursive, odd_recursive = even_odd_recursive(num_list)

# Output the results
print("\nList of All Numbers:", num_list)
print("List of Even Numbers (Iterative):", even_list)
print("List of Odd Numbers (Iterative):", odd_list)
print("\nList of Even Numbers (Recursive):", even_recursive)
print("List of Odd Numbers (Recursive):", odd_recursive)
