#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
#Exp 3.2 : Factorial Generator
def factorail(n):
    if n == 0 or n == 1:
        return 1
    else:
       return n * (factorail(n-1))
    
number = int(input("Enter the number: "))
print(factorail(number))