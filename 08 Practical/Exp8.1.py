# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 8.1: Script to Validate Phone Number and Email ID

import re

def validate_contact_info():
    print("--- Contact Info Validator ---")
    
    # Phone Number Regex: 10 digits, optional country code
    phone_regex = r"^(\+91[\-\s]?)?[6-9]\d{9}$"
    
    # Email Regex: Standard email pattern
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    phone = input("Enter Phone Number: ")
    if re.match(phone_regex, phone):
        print("Valid Phone Number.")
    else:
        print("Invalid Phone Number.")

    email = input("Enter Email ID: ")
    if re.match(email_regex, email):
        print("Valid Email ID.")
    else:
        print("Invalid Email ID.")

if __name__ == "__main__":
    validate_contact_info()
