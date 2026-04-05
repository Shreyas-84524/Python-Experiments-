#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Exp 4.3: Character Type Identifier
def identify_character_type():
    char = input("Enter a single character: ")
    
    if len(char) != 1:
        print("Please enter exactly one character.")
        return
    if char.isdigit():
        print(f"'{char}' is a Digit.")
    elif char.islower():
        print(f"'{char}' is a Lowercase Letter.")
    elif char.isupper():
        print(f"'{char}' is an Uppercase Letter.")
    else:
        print(f"'{char}' is a Special Character.")

if __name__ == "__main__":
    identify_character_type()