#Shreyas Rajenrda Shigwan, Roll no. 90, CSE(AIML)
# Exp 5.2: Custom Exceptions in Banking Systems 
class InsufficientBalance(Exception):
    pass
balance = 5000
try:
    amount = int(input("Enter withdrawl amount : "))
    if amount > balance:
        raise InsufficientBalance
    balance -= amount
    print("Remaining Balance:", balance)
except InsufficientBalance:
    print("Error : Insufficient Balance")