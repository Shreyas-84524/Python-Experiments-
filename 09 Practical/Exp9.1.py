# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 9.1: Creating and Manipulating Arrays

import numpy as np 
def array_operations():
    print("--- NumPy Array Operations ---")

    # 1D Array
    arr1 = np.array([1, 2, 3, 4, 5, 6])
    print("\n1D Array:")
    print(arr1)
    
    # 2D Array
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("\n2D Array:")
    print(arr2)
    
    # 3D Array
    arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print("\n3D Array:")
    print(arr3)

    # Reshaping
    print("\nReshaping 1D array to 2x3 matrix:")
    reshaped_arr = arr1.reshape(2, 3)
    print(reshaped_arr)

    # Slicing
    print("\nSlicing 1D Array (index 1 to 4):")
    print(arr1[1:4])
    
    print("\nSlicing 2D Array (Row 0, Column 1):")
    print(arr2[0, 1])

    # Indexing
    print("\nIndexing 3D Array (Depth 1, Row 0, Col 1):")
    print(arr3[1, 0, 1])

if __name__ == "__main__":
    try:
        array_operations()
    except ImportError:
        print("NumPy is not installed. Please install it using: pip install numpy")
