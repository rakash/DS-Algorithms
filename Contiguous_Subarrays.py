# Contiguous Sub-arrays

def count_subarrays(arr):
    output = [1] * len(arr)
    for i in range(len(arr)):
        print(f"i is {i}")
        k = i
        while k - 1 >= 0 and arr[k - 1] < arr[i]:
            output[i] += 1
            print(output[i])
            k -= 1
        print(f"output 1 is {output}")
        k = i
        while k + 1 < len(arr) and arr[k + 1] < arr[i]:
            output[i] += 1
            k += 1
        print(f"output 2 is {output}")
    return output

test_1 = [3, 4, 1, 6, 2]
expected_1 = [1, 3, 1, 5, 1]

test_2 = [2, 4, 7, 1, 5, 3]
expected_2 = [1, 2, 6, 1, 3, 1]

print(count_subarrays(test_1))
print(count_subarrays(test_2))