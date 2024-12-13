# Q.3 Reverse a number ?

# input from the user
num = int(input("Enter the number: "))

# initialzed variable for storing reversed the numbers 
rev_num = 0

# reverse process
while num > 0:
    digit = num % 10 # getting the last digit
    rev_num = rev_num * 10 + digit # creating reverse number
    num = num // 10 # for removing the last digit
    
# printing the reversed number
print("The reverse of the numnber is: ",rev_num)
