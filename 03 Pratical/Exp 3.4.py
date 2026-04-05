#Shreyas Rajendra Shigwan, Roll no. 90, ,CSE(AIML)
#Exp 3.4 : Simple Calculator Using Functions

n = int(input("Enter number : "))
j = int(input("Enter number : "))
choice = int(input("1 for addition, \n2 for sub, \n3 for multi, \n4 for division, \n5 for modules \n"))
if choice == 1:
    print(n+j)
elif choice == 2:
    print(n-j)
elif choice == 3:
    print(n*j)
elif choice == 4:
    print(n/j)
elif choice == 5:
    print(n%j)
else:
    print("Invalid text choice from (1/2/3/4/5)")