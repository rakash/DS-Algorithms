# 3.4 Pair Sums
import math
from collections import Counter

def numberOfWays(arr, k):
    d = Counter(arr)
    print(d)
    num_times = 0
    for key in d:
        print(key)
        if k - key in d:
            if k - key == key:
                val = d[key]
                print('val')
                print(val)
                num_times += val*(val-1)/2
            else:
                num_times += d[key] * d[k-key] / 2
    return num_times

k_1 = 6
arr_1 = [1, 2, 3, 4, 3]
expected_1 = 2
print(numberOfWays(arr_1, k_1))

k_2 = 6
arr_2 = [1, 5, 3, 3, 3]
expected_2 = 4
print(numberOfWays(arr_2, k_2))
