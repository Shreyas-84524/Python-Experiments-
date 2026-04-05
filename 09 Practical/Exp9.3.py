# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 9.3: Statistical Operations

import numpy as np

def statistical_ops():
    print("--- NumPy Statistical Operations ---")
    
    data = np.array([15, 20, 25, 30, 35, 40, 45, 50])
    print(f"Data: {data}")
    
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard Deviation: {np.std(data)}")
    print(f"Variance: {np.var(data)}")
    
    data2 = np.array([10, 15, 20, 25, 30, 35, 40, 45])
    print(f"\nData 2: {data2}")
    
    corr_matrix = np.corrcoef(data, data2)
    print("Correlation Coefficient Matrix:")
    print(corr_matrix)
    print(f"Correlation between Data and Data2: {corr_matrix[0, 1]}")

if __name__ == "__main__":
    try:
        statistical_ops()
    except ImportError:
        print("NumPy is not installed. Please install it using: pip install numpy")
