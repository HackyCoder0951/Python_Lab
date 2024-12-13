from collections import Counter

def add_numbers(num):
    t_sum = 0
    for i in range(num):
        value = int(input(f"Enter {i+1} element : "))
        num_list.append(value)  # assigning values into num_list[]
        t_sum += value
    return t_sum

def add_numbers_recursive(rec_num, index=0):
    if index >= rec_num:  # Base case: if index is equal to num, return 0
        return 0
    else:
        value = int(input(f"Enter {index + 1} element: "))
        num_list.append(value)  # Assigning values into num_list[]
        return value + add_numbers_recursive(rec_num, index + 1)  # Recursive call

def count_numbers(numbers):
    """
    Counts the number of positive, negative, and zero values in the list.
    """
    positives = sum(1 for n in numbers if n > 0)
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
    #temp = num # temporary variable for num value assign
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

def draw_patterns(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()
    for i in range(1, n + 1):
        print("*" * i)
    print()
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
    return max(a, b, c)

def frequency_count(numbers):
    return dict(Counter(numbers))

def frequency_count_recursive(numbers, freq=None):
    if freq is None:
        freq = {}
    if not numbers:
        return freq
    freq[numbers[0]] = freq.get(numbers[0], 0) + 1
    return frequency_count_recursive(numbers[1:], freq)

# Input handling
def get_user_input():
    """
    Collects numbers from the user until 'd' is entered.
    """
    num_list = []
    print("Enter numbers to add to the list. Type 'd' to finish.")
    while True:
        user_input = input("Enter a number (or 'd' to finish): ").strip().lower()
        if user_input == 'd':
            break
        if user_input.replace('.', '', 1).replace('-', '', 1).isdigit():
            num_list.append(float(user_input) if '.' in user_input else int(user_input))
        else:
            print("Invalid input. Please enter a valid number.")
    return num_list

# Example usage of functions
if __name__ == "__main__":
    num_list=[]
    # Taking input from the user