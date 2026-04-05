#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Exp 4.7: Prime Number Analyzer

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_analyzer():
    print("--- Prime Number Analyzer ---")
    try:
        num = int(input("Enter a number: "))
        if check_prime(num):
            print(f"{num} is a Prime Number.")
        else:
            print(f"{num} is NOT a Prime Number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    prime_analyzer()
