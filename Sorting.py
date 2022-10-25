# 7- Sorting

## Bubble Sort

def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp
    
def bubblesort(array):
    sorted=False
    final_index = len(array) - 1
    while not sorted:
        sorted = True
        for index in range(final_index):
            if array[index] > array[index + 1]:
                swap(array, index, index + 1)
                sorted = False
        final_index -= 1
                
array = [3, 1, 2, 5, 7, 4, 4]
print(array)
bubblesort(array)
print(array)

## Merge Sort

import math

def copyback(array, helper, offset):
    for i in range(len(helper)):
        array[offset + i] = helper[i]

def mergeback(array, left_start, right_start, right_end):
    helper = [0] * (right_end - left_start + 1) 
    left_index = left_start
    right_index = right_start
    
    for index in range(len(helper)):
        # give me left if appropriate else right
        if right_index > right_end or (left_index < right_start and array[left_index] <= array[right_index]):
            helper[index] = array[left_index]
            left_index += 1
        else:
            helper[index] = array[right_index]
            right_index += 1
    return helper

def mergesort_helper(array, left, right):
    if right <= left:
        return 
    
    middle = math.floor((left + right) / 2)
    mergesort_helper(array, left, middle)
    mergesort_helper(array, middle + 1, right)
    helper = mergeback(array, left, middle + 1, right)
    copyback(array, helper, left)
    
def mergesort(array):
    mergesort_helper(array, 0, len(array) - 1)
    
array = [3, 1, 2, 5, 7, 4, 4]
print(array)
mergesort(array)
print(array)

## Balanced Split

def balancedSplitExists(arr: list) -> bool: 
    # [1, 5, 7, 1]
    arr.sort()  ## O(nlogn)
    # [1, 1, 5, 7]
    
    arr_cumsum = arr.copy()
    for i in range(1, len(arr_cumsum)):
        arr_cumsum[i] += arr_cumsum[i-1]
    for i in range(len(arr) - 1):
        if arr_cumsum[i]*2 == arr_cumsum[-1] and arr[i] != arr[i+1]:
            return True
    return False
    
arr_1 = [2, 1, 2, 5]
expected_1 = True
print(balancedSplitExists(arr_1))

arr_2 = [3, 6, 3, 4, 4]
expected_2 = False
print(balancedSplitExists(arr_2))

# Counting Triangles

## Method 1 
def countDistinctTriangles(arr: list):
    triangles = set()
    for t in arr:
        triangles.add(tuple(sorted(t))) # Sort on a tuple gives a list
    return len(triangles)

## Method 2

def countDistinctTriangles(arr: list):
    return len(set(map(lambda t: tuple(sorted(t)), arr)))

    