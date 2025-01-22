text = "String 1234.5"

uppercase = 0
lowercase = 0
digit = 0
whitespace = 0

for i in text:
    if (i.isupper()):
        uppercase += 1
    elif (i.islower()):
        lowercase += 1
    elif (i.isdigit()):
        digit += 1
    elif (i.isspace()):
        whitespace += 1
    
word_count = len(text.split())

print(f"Given string is - '{text}' ")
print(f"Number of uppercase letters:{uppercase}")
print(f"Number of lowercase letters:{lowercase}")
print(f"Number of digits:{digit}")
print(f"Number of whitespaces:{whitespace}")
print(f"Number of Word Counts:{word_count}")