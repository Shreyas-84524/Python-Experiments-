#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Exp 4.6: Factorial Generator

def factorial_generator():
    print("--- Factorial Generator ---")
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Factorial does not exist for negative numbers.")
        elif n == 0:
            print("The factorial of 0 is 1")
        else:
            factorial = 1
            for i in range(1, n + 1):
                factorial = factorial * i
            print(f"The factorial of {n} is {factorial}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    factorial_generator()
