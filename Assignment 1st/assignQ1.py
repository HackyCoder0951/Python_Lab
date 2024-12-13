# Q.1 Sum of N natural numbers ?

n = int(input("Enter the total number of elements to be added : ")) # total size of n numbers

sum = 0 # for value assign of addition of total n numbers

for i in range(n):
  
    value = int(input(f"Enter {i+1} number : ")) # entering numbers according to total size of n numbers
  
    sum += value # addition of total n numbers
  
print("The Sum is",sum)
