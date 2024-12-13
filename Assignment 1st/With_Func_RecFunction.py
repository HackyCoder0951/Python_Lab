from collections import Counter

# 1. Add n Numbers
def add_numbers(numbers):
    return sum(numbers)

# 2. Count Positive, Negative, and Zeros
def count_numbers(numbers):
    positives = sum(1 for n in numbers if n > 0)
    negatives = sum(1 for n in numbers if n < 0)
    zeros = sum(1 for n in numbers if n == 0)
    return positives, negatives, zeros

def count_numbers_recursive(numbers, pos=0, neg=0, zero=0):
    if not numbers:
        return pos, neg, zero
    if numbers[0] > 0:
        return count_numbers_recursive(numbers[1:], pos + 1, neg, zero)
    elif numbers[0] < 0:
        return count_numbers_recursive(numbers[1:], pos, neg + 1, zero)
    else:
        return count_numbers_recursive(numbers[1:], pos, neg, zero + 1)

# 3. Reverse a Number
def reverse_number(number):
    return int(str(number)[::-1])

def reverse_number_recursive(number, rev=0):
    if number == 0:
        return rev
    return reverse_number_recursive(number // 10, rev * 10 + number % 10)

# 4. Sum of Digits
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def sum_of_digits_recursive(number):
    if number == 0:
        return 0
    return number % 10 + sum_of_digits_recursive(number // 10)

# 5. Separate Even and Odd Numbers
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

# 6. Factorial and Palindrome Check
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

# 7. Draw Patterns
def draw_patterns(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()
    for i in range(1, n + 1):
        print("*" * i)
    print()
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

# 8. Find Maximum and Minimum in a List
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

# 9. Find Maximum of Three Numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# 10. Frequency Count of Each Element

# from collections import Counter

def frequency_count(numbers):
    return dict(Counter(numbers))

def frequency_count_recursive(numbers, freq=None):
    if freq is None:
        freq = {}
    if not numbers:
        return freq
    freq[numbers[0]] = freq.get(numbers[0], 0) + 1
    return frequency_count_recursive(numbers[1:], freq)

# Example usage of functions
if __name__ == "__main__":
    # Example inputs
    numbers = [3, -2, 0, 5, 0, -1]
    print("Add Numbers:", add_numbers(numbers))
    print("Count Numbers:", count_numbers(numbers))
    print("Recursive Count Numbers:", count_numbers_recursive(numbers))
    print("Reverse Number:", reverse_number(12345))
    print("Recursive Reverse Number:", reverse_number_recursive(12345))
    print("Sum of Digits:", sum_of_digits(12345))
    print("Recursive Sum of Digits:", sum_of_digits_recursive(12345))
    print("Separate Even and Odd:", separate_even_odd(numbers))
    print("Recursive Separate Even and Odd:", even_odd_recursive(numbers))
    print("Factorial:", factorial(5))
    print("Recursive Factorial:", factorial_recursive(5))
    print("Is Palindrome:", is_palindrome(121))
    print("Draw Patterns:")
    draw_patterns(5)
    print("Find Max and Min:", find_max_min(numbers))
    print("Recursive Max:", find_max_recursive(numbers))
    print("Recursive Min:", find_min_recursive(numbers))
    print("Max of Three Numbers:", max_of_three(3, 7, 5))
    print("Frequency Count:", frequency_count(numbers))
    print("Recursive Frequency Count:", frequency_count_recursive(numbers))
