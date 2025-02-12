# Q 2.2 - WAP that accepts a string to setup a passwords. 
# Your entered password must meet the following requirements :
    # 1 - The password must be at least 8 characters long.
    # 2 - The password must contain at least one uppercase letter.
    # 3 - The password must contain at least one lowercase letter.
    # 4 - The password must contain at least one numeric digit.
    # 5 - The password must contain at least one special symbol (e.g., $, @, #, %).

# Function for password validation
def is_valid_password(password):
    # Check the length of the password
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Flags for validation
    has_uppercase = any(i.isupper() for i in password) # for checking uppercase letters
    has_lowercase = any(i.islower() for i in password) # for checking lowercase letters
    has_digit = any(i.isdigit() for i in password) # for checking digits
    has_symbol = any(char in '$@#%' for char in password) # for checking special symbols
    
    # Validate all requirements
    if not has_uppercase:
        return "Password must contain at least one uppercase letter."
    elif not has_lowercase:
        return "Password must contain at least one lowercase letter."
    elif not has_digit:
        return "Password must contain at least one numeric digit."
    elif not has_symbol:
        return "Password must contain at least one special symbols."
    else :
        return "Password is valid!"

# Input password from user
password = input("Enter your password: ")

# Check and display the result
result = is_valid_password(password)
print(result)
