#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Exp 5.4: Using a Debugger


import pdb

def sum_list(numbers):
    total = 0
    # Intentional Logic Error: starting index might be wrong or loop logic for debugging
    for i in range(len(numbers)):
        
        val = numbers[i]
        total += val
    return total

def debug_demo():
    print("--- Debugger Demo ---")
    data = [10, 20, 30, "40", 50] # Intentional Error: string in list
    
    print("Starting calculation...")
    # pdb.set_trace() # Start debugger
    
    try:
        result = sum_list(data)
        print(f"Sum: {result}")
    except TypeError as e:
        print(f"Caught an error: {e}")
        print("Tip: Use 'pdb' to inspect the 'data' list and finding the bad value.")
        print("Run this script with: python -m pdb exp_4_debugger.py")

if __name__ == "__main__":
    debug_demo()
