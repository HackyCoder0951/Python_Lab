# Q.6 find factorial & check palindrome numbers?

from recursiveFuncModule import factorial,factorial_recursive,is_palindrome,is_palindrome_recursive
num = int(input("Enter Number you want to check : "))
##### Factorial Number #####
fact = 1 # initialized factiorial as 1 because multiplying any number by 1 doest not change its value
for i in range(1,num+1): # loop for generation of numbers from 1 to given number ( inclusive)
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
iterative_fact = factorial(num)
print(f"The factorial of {num} (Iterative) is: {iterative_fact}")
# Using the recursive `factorial_recursive` function
recursive_fact = factorial_recursive(num)
print(f"The factorial of {num} (Recursive) is: {recursive_fact}")
print("Palindrome Check using Iterative & Recursive Function")
# Using the `is_palindrome` function
if is_palindrome(num):
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number.")  
# Using the recursive `is_palindrome_recursive` function
# Call the recursive function
if is_palindrome_recursive(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")