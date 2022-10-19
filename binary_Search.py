# 5 - Search

### Recursive solution -- Costly
import math
def binarysearch_helper(target, array, left, right):
    if right < left:
        return -1
    middle = math.floor((left+right) /2)
    
    if array[middle] == target:
        return middle
    elif target < array[middle]:
        return binarysearch_helper(target, array, left, middle - 1)
    else:
        return binarysearch_helper(target, array, middle + 1, right)
    
def binarysearch(target, array):
    return binarysearch_helper(target, array, 0, len(array) - 1)

### Iterative solution -- Better

def binarysearch(target, array):
    left = 0
    right = len(array) -1 
    
    while left <= right:
        middle = math.floor((left + right) / 2)
        
        if array[middle] == target:
            return middle
        elif target < array[middle]: # search left
            right = middle -1
        else:
            left = middle + 1
    return -1

array = [1, 5, 681, 2, 8, 9, 32, -5, -9, 6, 100, 102, 392]
sorted_Array = sorted(array)
print(sorted_Array)

print(binarysearch(sorted_Array[0] - 1, sorted_Array))

for target in sorted_Array:
    print(binarysearch(target, sorted_Array))

print(binarysearch(sorted_Array[-1] + 1, sorted_Array))

sarray = [1, 5]

f = open("/output.txt", "w")
for item in sarray:
   f.write(item + "\n")
f.close()
