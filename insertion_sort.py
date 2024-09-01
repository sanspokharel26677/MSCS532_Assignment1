"""
File: insertion_sort.py
Author: Sandesh Pokharel
Date: 2024-08-31
Description: This is program for the Insertion Sort Algorithm that sorts in monotonically decreasing order
"""

def insertion_sort_monotonically_decreasing(arr):
    """
    Sorts an array in monotonically decreasing order using the Insertion Sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list in monotonically decreasing order.
    """
    # Traversing from the second element to the end of the list
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Moving elements of arr[0..i-1] that are less than key to one position ahead of their original position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # This will be placing key in the correct position
        arr[j + 1] = key
    
    return arr
    
    #Using algorithm
if __name__ == "__main__":
    data = [10,3,2,5,8,4,3,1]
    print("Original array:", data)
    sorted_data = insertion_sort_monotonically_decreasing(data)
    print("Sorted array in decreasing order:", sorted_data)
