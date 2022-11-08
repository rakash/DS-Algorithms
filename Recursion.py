import timeit

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n -2)

max = 40
for n in range(0, max):
    t = timeit.Timer(lambda: fibonacci(n))
    time = t.timeit(1)
    print("fib({0}) took {1} time".format(n, time))
    
## The above code shows that as N slowly increases, it becomes slower. Run the code to check.    

## Encrypted Words

import math

def findEncryptedWord(s):
    if s == '':
        return s
    if len(s) % 2 == 1: #odd
        m = int((len(s) - 1)/2)
    else:
        m = int(len(s)/2 - 1)
    return s[m] + findEncryptedWord(s[:m]) + findEncryptedWord(s[m+1:])
  
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
    global test_case_number
    result = False
  
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1

if __name__ == "__main__":
    s1 = "abc"
    expected_1 = "bac"
    output_1 = findEncryptedWord(s1)
    check(expected_1, output_1)

    s2 = "abcd"
    expected_2 = "bacd"
    output_2 = findEncryptedWord(s2)
    check(expected_2, output_2)

# Change in a foreign currency

def canGetExactChange(targetMoney: int, denominations: list):
    # Write your code here  
    if targetMoney == 0:
        return True
    if targetMoney < 0:
        return False

    for i in range(len(denominations)):
        if canGetExactChange(targetMoney - denominations[i], denominations[i:]):
            return True
    return False

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
  
    test_case_number += 1

if __name__ == "__main__":
    
    target_1 = 94
    arr_1 = [5, 10, 25, 100, 200]
    expected_1 = False
    output_1 = canGetExactChange(target_1, arr_1)
    check(expected_1, output_1)

    target_2 = 75
    arr_2 = [4, 17, 29]
    expected_2 = True
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)
