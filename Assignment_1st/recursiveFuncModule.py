global_list = []
def add_numbers(num):
    global global_list
    global_list.clear()
    t_sum = 0
    for i in range(num):
        value = int(input(f"Enter {i+1} element : "))
        global_list.append(value)  # assigning values into global_list[]
        t_sum += value
    return t_sum

def add_numbers_recursive(rec_num, index=0):
    global global_list
    global_list.clear()
    if index >= rec_num:  # Base case: if index is equal to num, return 0
        return 0
    else:
        value = int(input(f"Enter {index + 1} element: "))
        global_list.append(value)  # Assigning values into global_list[]
        return value + add_numbers_recursive(rec_num, index + 1)  # Recursive call

def count_numbers(numbers):
    """
    Counts the number of positive, negative, and zero values in the list.
    """
    # using generator expression concepts
    positives = sum(1 for n in numbers if n > 0) 
    # For every n that satisfies the condition n > 0, the value 1 is produced.
    negatives = sum(1 for n in numbers if n < 0) 
    zeros = sum(1 for n in numbers if n == 0)
    return positives, negatives, zeros


def count_numbers_recursive(numbers, pos=0, neg=0, zero=0):
    """
    Recursively counts the number of positive, negative, and zero values in the list.
    """
    if not numbers:
        return pos, neg, zero
    if numbers[0] > 0:
        return count_numbers_recursive(numbers[1:], pos + 1, neg, zero)
    elif numbers[0] < 0:
        return count_numbers_recursive(numbers[1:], pos, neg + 1, zero)
    else:
        return count_numbers_recursive(numbers[1:], pos, neg, zero + 1)


def reverse_number(number):
    return int(str(number)[::-1])

def reverse_number_recursive(number, rev=0):
    if number == 0:
        return rev
    return reverse_number_recursive(number // 10, rev * 10 + number % 10)

def sum_of_digits(num):
    n_sums = 0 # variable for sum of digit
    while(num>0):
        digit = num % 10 # calculates the last digit of number
        n_sums += digit # addition of last digit obtained in uper line
        num //= 10 # integer division of num by 10 so it will automatically remove the last digit of num
    return n_sums

def sum_of_digits_recursive(number):
    if number == 0:
        return 0
    return number % 10 + sum_of_digits_recursive(number // 10)

def separate_even_odd(numbers):
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    return even, odd

def even_odd_recursive(numbers, even=[], odd=[]):
    if not numbers:
        return even, odd
    if numbers[0] % 2 == 0:
        even.append(numbers[0])
    else:
        odd.append(numbers[0])
    return even_odd_recursive(numbers[1:], even, odd)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def is_palindrome_recursive(n, temp=None):
    # Initialize the temp variable on the first call
    if temp is None:
        temp = n   
    # Base case: If n is reduced to 0, stop the recursion
    if n == 0:
        return temp == 0   
    # Get the last digit of the number and compare it with the first digit
    last_digit = n % 10
    first_digit = temp % 10
    # If the digits do not match, it's not a palindrome
    if last_digit != first_digit:
        return False  
    # Remove the first and last digit and call the function recursively
    return is_palindrome_recursive(n // 10, temp // 10)

def draw_patterns(n):
    print("\nPattern 1 using function")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()
    print("\nPattern 2 using function")
    for i in range(1, n + 1):
        print("*" * i)
    print()
    print("\nPattern 3 using function")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

def find_max_min(numbers):
    return max(numbers), min(numbers)

def find_max_recursive(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return max(numbers[0], find_max_recursive(numbers[1:]))

def find_min_recursive(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return min(numbers[0], find_min_recursive(numbers[1:]))

def max_of_three(a, b, c):
    """Returns the maximum of three numbers."""
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Function to count frequency using iteration
def frequency_count(numbers):
    """
    Counts the frequency of each element in the list using iteration.
    Returns a dictionary with the frequency of each element.
    """
    frequency = {}
    for element in numbers:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

# Function to count frequency using recursion
def frequency_count_recursive(numbers, frequency=None):
    if frequency is None:
        frequency = {}   
    if not numbers:  # Base case: if the list is empty, return the frequency dictionary
        return frequency  
    # Get the first element in the list
    element = numbers[0]    
    # Update the frequency dictionary
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1
    # Recurse with the rest of the list
    return frequency_count_recursive(numbers[1:], frequency)

# List Input handling without defining parameters inside function
def get_user_input():
    """
    Collects numbers from the user until 'd' is entered.
    """
    global global_list
    global_list.clear()
    print("Enter numbers to add to the list. Type 'd' to finish.")
    while True:
        user_input = input("Enter a number (or 'd' to finish): ").strip().lower()
        if user_input == 'd':
            break
        if user_input.replace('.', '', 1).replace('-', '', 1).isdigit():
            global_list.append(float(user_input) if '.' in user_input else int(user_input))
        else:
            print("Invalid input. Please enter a valid number.")
    return global_list

# List Input handling with defining parameters inside function
def get_number_list(n):
    """
    Collects a list of numbers from the user.
    :param n: Total number of elements in the list
    :return: A list of numbers entered by the user
    """
    global global_list
    global_list.clear()
    for i in range(n):
        value = int(input(f"Enter element {i + 1}: "))
        global_list.append(value)
    return global_list

#For Example : execute this as seperate scipt
if __name__ == "__main__":
    get_user_input()
    print("\nInputed List : ->",global_list,"\n")