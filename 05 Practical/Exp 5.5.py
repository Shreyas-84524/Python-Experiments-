#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Exp 5.5: Scientific Debugging Techniques
def binary_search(arr, target):
    low = 0
    high = len(arr) # Error 1: Should be len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid 
            
    return -1

def buggy_program():
    print("--- Scientific Debugging Practice ---")
    my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_val = 23
    
    print(f"List: {my_list}")
    print(f"Target: {target_val}")
    
    try:
        index = binary_search(my_list, target_val)
        if index != -1:
            print(f"Found at index: {index}")
        else:
            print("Not found.")
    except Exception as e:
        print(f"Crashed with error: {e}")
        print("Task: Use print debugging or a debugger to find the off-by-one errors.")

if __name__ == "__main__":
    buggy_program()
