import re

def validate_email(email):
    # Regular expression for validating email
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None

# Take email input from the user
user_email = input("Enter an email address to validate: ")

if validate_email(user_email):
    print(f"{user_email} is a Valid email address.")
else:
    print(f"{user_email} is an Invalid email address.")
