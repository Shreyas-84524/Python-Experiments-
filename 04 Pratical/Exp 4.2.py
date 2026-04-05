#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
#Exp 4.2 : Number type identifier (Even or Odd)

def check_even_odd():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    check_even_odd()