#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
#Exp 3.3 : Prime number Analyzer

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True   

number = int(input("Enter a number: "))
if prime(number):
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime")