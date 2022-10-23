# 6 - Binary Search - 1B users

import math

def f(rates, t):
    return sum(r**t for r in rates)

def getBillionUsersDay(rates: list):
    lo = 1
    hi = 1
    bil = 1_000_000_000
    while f(rates, hi) <= bil:
        hi *= 10
    
    while hi - lo > 1:
        mi = (lo + hi)/2
        if f(rates, mi) < bil:
            lo = mi
        else:
            hi = mi
    #f(rates, lo) < bil, f(rates, hi) > bil
    if f(rates, math.floor(hi)) >= bil:
        return math.floor(hi)
    return math.ceil(hi)
    
test_1 = [1.1, 1.2, 1.3]
expected_1 = 79
print(getBillionUsersDay(test_1))

test_2 = [1.01, 1.02]
expected_2 = 1047
print(getBillionUsersDay(test_2))