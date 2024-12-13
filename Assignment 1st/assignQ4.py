# Q.4 sum of digits of a number ?

num = int(input("Enter a number : ")) 

temp = num # temporary variable for num value assign

sum = 0 # variable for sum of digit

while(num>0):

    digit = num % 10 # calculates the last digit of number

    sum += digit # addition of last digit obtained in uper line
    
    num //= 10 # integer division of num by 10 so it will automatically remove the last digit of num

print("The sum of digits of",temp,"is",sum)
