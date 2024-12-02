import re

def validate_email(email):
    # Regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Match the email against the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
email = input("Enter an email address: ")

if validate_email(email):
    print(f"'{email}' is a valid email address.")
else:
    print(f"'{email}' is not a valid email address.")
