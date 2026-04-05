#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML) 
#Exp 4.1 : Triangle pattern generator

def print_triangle_pattern():
    try:
        rows = int(input("Enter number of rows: "))
        print("\nPattern:")
        for i in range(1, rows + 1):
            print("SS " * i)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    print_triangle_pattern()