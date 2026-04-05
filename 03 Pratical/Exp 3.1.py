#SHreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
#Exp 3.1 : Number Type Identifier
while True:
    num = int(input("Enter the num: "))

    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

    choice = input("Do you want to continue the check (yes/no): ").lower()
    if choice != "yes":
        print("Exit the program")
        break