#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Exp 4.5: Fibonacci Sequence Generator


def fibonacci_generator():
    print("--- Fibonacci Sequence Generator ---")
    try:
        n_terms = int(input("How many terms? "))

        n1, n2 = 0, 1
        count = 0

        if n_terms <= 0:
            print("Please enter a positive integer")
        elif n_terms == 1:
            print(f"Fibonacci sequence upto {n_terms}:")
            print(n1)
        else:
            print("Fibonacci sequence:")
            while count < n_terms:
                print(n1, end=" ")
                nth = n1 + n2
                # update values
                n1 = n2
                n2 = nth
                count += 1
            print() # Newline at the end
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    fibonacci_generator()

