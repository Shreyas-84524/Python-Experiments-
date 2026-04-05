# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Exp 1.1 : Arithmetic Calculator

def arithmetic_operations():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("\nResults:")
    print(f"Addition ({num1} + {num2}) = {num1 + num2}")
    print(f"Subtraction ({num1} - {num2}) = {num1 - num2}")
    print(f"Multiplication ({num1} * {num2}) = {num1 * num2}")
    
    if num2 != 0:
        print(f"Division ({num1} / {num2}) = {num1 / num2}")
        print(f"Modulus ({num1} % {num2}) = {num1 % num2}")
        print(f"Floor Division ({num1} // {num2}) = {num1 // num2}")
        print(f"Exponentiation ({num1} ** {num2}) = {num1 ** num2}")
    else:
        print("Division, Modulus, Floor Division by zero is not defined.")

if __name__ == "__main__":
    arithmetic_operations()
