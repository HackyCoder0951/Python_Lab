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
