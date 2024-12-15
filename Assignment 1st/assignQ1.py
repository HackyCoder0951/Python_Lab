# Q.1 Sum of N natural numbers ?

from recursiveFuncModule import add_numbers,add_numbers_recursive

# total size of n numbers
n = int(input("Enter the total number of elements to be added : ")) 

# for value assign of addition of total n numbers
sum_num = 0 

for i in range(n):
    
    # entering numbers according to total size of n numbers
    i = int(input(f"Enter {i+1} number : ")) 
    
    # addition of total n numbers
    sum_num += i 
  
print("Add Numbers using normal method :",sum_num)

print("Add Numbers using function :", add_numbers(n))

print("Add Numbers using recurve function :", add_numbers_recursive(n))