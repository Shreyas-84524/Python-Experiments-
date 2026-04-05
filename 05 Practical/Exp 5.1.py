#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
#Exp 5.1 : Basic Exception Handling

try:
    a = int(input("Enter numerator : "))
    b = int(input("Ent Denominator : "))
    result = a/b
    print("Result =", result)
except ZeroDivisionError:
    print("Error : Division by Zero")
except ValueError:
    print("Error : Invalid Input")