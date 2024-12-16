# Q.6 find factorial & check palindrome numbers?

import recursiveFuncModule 
num = int(input("Enter Number you want to check : "))
##### Factorial Number #####
fact = 1 # initialized factiorial as 1 because multiplying any number by 1 doest not change its value
for i in range(1,num+1): 
  fact *= i # multipy the factorial by the current number
print(f"The factorial of {num} is : {fact}")
##### Palindrome Numbers #####
original_num = str(num) # converting the number to string
rev_num  = original_num[::-1] # reversing the string using slicing
if original_num == rev_num : # compare the original string and reversed string
  print(f"{num} is a Palindrome number.")
else :
  print(f"{num} is not a Palindrome number.")
  
print("Factorial Calculation using Iterative & Recursive Function")
# Using the iterative `factorial` function
iterative_fact = recursiveFuncModule .factorial(num)
print(f"The factorial of {num} (Iterative) is: {iterative_fact}")
# Using the recursive `factorial_recursive` function
recursive_fact = recursiveFuncModule.factorial_recursive(num)
print(f"The factorial of {num} (Recursive) is: {recursive_fact}")

print("Palindrome Check using Iterative & Recursive Function")
# Using the `is_palindrome` function
if recursiveFuncModule.is_palindrome(num):
    print(f"{num} is a Palindrome (Iterative) number.")
else:
    print(f"{num} is not a Palindrome (Iterative) number.")  
# Using the recursive `is_palindrome_recursive` function
# Call the recursive function
if recursiveFuncModule.is_palindrome_recursive(num):
    print(f"{num} is a palindrome  (Recursive) number.")
else:
    print(f"{num} is not a palindrome  (Recursive) number.")