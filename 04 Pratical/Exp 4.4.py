#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Exp 4.4: Multiplication Table Generator
def multiplication_table():
    try:
        num = int(input("Enter a number: "))
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    multiplication_table()

