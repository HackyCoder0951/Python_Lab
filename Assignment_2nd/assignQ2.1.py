# Q 2.1 - WAP that reads a text from keyboard and display:
# A - The number of uppercase letters
# B - The number of lowercase letters
# C - The number digits
# D - The number of whitespace characters
# E - The number of words in the string

# Input text from the user
text = input("Enter a text : ")

# Initialize counters
uppercase_count = 0
lowercase_count = 0
digit_count = 0
whitespace_count = 0
word_count = 0

# Loop through each character in the text
for i in text:
    if (i.isupper()) and (i>='A' and i<='Z'):
        uppercase_count += 1
    elif (i.islower()) and (i>='a'and i<='z'):
        lowercase_count += 1
    elif (i.isdigit()) and (i>='0'and i<='9'):
        digit_count += 1
    elif (i.isspace()) and (i==' '):
        whitespace_count += 1
        
# Count the number of words
word_count = len(text.split())

# Display the results

print(f"The given string is : {text}")
print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")
print(f"Number of digits: {digit_count}")
print(f"Number of whitespace characters: {whitespace_count}")
print(f"Number of words: {word_count}")
