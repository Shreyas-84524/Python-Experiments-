# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 8.3: URL Validator

import re

def validate_url():
    print("--- URL Validator ---")
    url = input("Enter a URL to validate: ")
    
    url_regex = r"^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/.*)?$"

    if re.match(url_regex, url):
        print("Valid URL.")
    else:
        print("Invalid URL.")

if __name__ == "__main__":
    validate_url()
