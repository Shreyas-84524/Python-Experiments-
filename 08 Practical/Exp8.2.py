# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 8.2: Password Strength Checker

import re

def check_password_strength():
    print("--- Password Strength Checker ---")
    password = input("Enter a password: ")
    
    if len(password) < 8:
        print("Weak: Password must be at least 8 characters long.")
        return

    if not re.search(r"[a-z]", password):
        print("Weak: Must contain at least one lowercase letter.")
        return
        
    if not re.search(r"[A-Z]", password):
        print("Weak: Must contain at least one uppercase letter.")
        return

    if not re.search(r"\d", password):
        print("Weak: Must contain at least one digit.")
        return

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Weak: Must contain at least one special character.")
        return

    print("Strong Password! Good job.")

if __name__ == "__main__":
    check_password_strength()
