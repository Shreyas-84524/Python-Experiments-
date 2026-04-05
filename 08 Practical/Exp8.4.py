# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 8.4: Extracting Data from Text

import re
import os

def extract_data_from_file():
    print("--- Data Extractor ---")
    filename = "data_sourc.txt"
    
    # Create dummy file
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("Here is some contact info:\n")
            f.write("Shreyas: shreyas@example.com, +91-9869789060\n")
            f.write("Bablu's birthday is 02/12/2007.\n")
            f.write("Contact support at support@tech.com or call 9876543210.\n")
            f.write("Meeting on 2024-10-15.\n")
        print(f"Created '{filename}' for testing.")

    try:
        with open(filename, "r") as f:
            content = f.read()
            
        print("\n--- Extracted Emails ---")
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)
        print(emails)
        
        print("\n--- Extracted Phone Numbers ---")
        phones = re.findall(r"(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", content)
        # Cleaning up phone matches (regex return tuples sometimes)
        clean_phones = [p[0]+p[1] if isinstance(p, tuple) else p for p in phones] 
        # A simpler regex for 10 digits might be better for this specific demo
        simple_phones = re.findall(r"\b\d{10}\b", content)
        print(simple_phones)

        print("\n--- Extracted Dates ---")
        # Matches DD/MM/YYYY or YYYY-MM-DD
        dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b", content)
        print(dates)
        
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    extract_data_from_file()
