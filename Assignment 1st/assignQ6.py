# Q.6 find factorial & check palindrome numbers?

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
