# Input text from the user
text = input("Enter a text 0951")

# Initialize counters
uppercase_count = 0
lowercase_count = 0
digit_count = 0
whitespace_count = 0

# Loop through each character in the text
for char in text:
    if (char.isupper()) or (char>='a'and char<='z'):
        uppercase_count += 1
    elif (char.islower()) or (char>='A'and char<='Z'):
        lowercase_count += 1
    elif (char.isdigit()) or (char>='0'and char<='9'):
        digit_count += 1
    elif (char.isspace()) or (char==' '):
        whitespace_count += 1

# Count the number of words
word_count = len(text.split())

# Display the results
print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")
print(f"Number of digits: {digit_count}")
print(f"Number of whitespace characters: {whitespace_count}")
print(f"Number of words: {word_count}")
