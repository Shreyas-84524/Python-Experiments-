# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Exp 9.2: Array Mathematics

import numpy as np

def array_math():
    print("--- NumPy Array Mathematics ---")
    
    # Create two arrays
    a = np.array([10, 20, 30])
    b = np.array([1, 2, 3])
    
    print(f"Array A: {a}")
    print(f"Array B: {b}")
    
    # Element-wise Operations
    print("\nAddition (A + B):", a + b)
    print("Subtraction (A - B):", a - b)
    print("Multiplication (A * B):", a * b)
    print("Division (A / B):", a / b)
    
    # Dot Product
    print("\nDot Product (A . B):", np.dot(a, b))
    
    # Cross Product
    print("Cross Product (A x B):", np.cross(a, b))

if __name__ == "__main__":
    try:
        array_math()
    except ImportError:
        print("NumPy is not installed. Please install it using: pip install numpy")