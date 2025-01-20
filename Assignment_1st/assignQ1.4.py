# Q.4 sum of digits of a number ?

from recursiveFuncModule import sum_of_digits,sum_of_digits_recursive
num = int(input("Enter a number : ")) 
temp = num # temporary variable for num value assign
n_sums = 0 # variable for sum of digit
while(temp>0):
   digit = temp % 10 # calculates the last digit of number
   n_sums += digit # addition of last digit obtained in uper line
   temp //= 10 # integer division of num by 10 so it will automatically remove the last digit of num      
print("The sum of digits of ",num,"is",n_sums,"\n")
print("Sum of digits using function & recursive function :")
# Calculate the sum of digits iteratively
iterative_sum = sum_of_digits(num)
print(f"The sum of digits of {num} using the iterative function is : {iterative_sum}\n")
# Calculate the sum of digits recursively
recursive_sum = sum_of_digits_recursive(num)
print(f"The sum of digits of {num} using the recursive function is : {recursive_sum}\n")