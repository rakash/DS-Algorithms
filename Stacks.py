class Node:
    def __init__(self, val):
        self.value = val
        self.next= None 
    
class Stack:
    def __init__(self):
        self.stack_size = 0
        self.top = None
    
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.stack_size += 1
        
    def pop(self):
        if self.top:
            self.stack_size -= 1
            value = self.top.value
            self.top = self.top.next
            return value
        else:
            raise Exception("Stack is empty")
        
    def peek(self):
        if self.top:
            return self.top.value
        raise Exception("Stack is empty")
    
    def size(self):
        return self.stack_size
    
stack = Stack()
array = [1, 2, 3, 4, 5]
for a in array:
    stack.push(a)

print(stack.size())
print("Stack top is {0}".format(stack.peek()))

for _ in range(len(array)):
    print(stack.pop())
    
print(stack.size())


## Valid String

class Solution:
    def checkvalid(self, s: str):
        stack = []
        mapping = {
            '(':')',
            '[':']',
            '{':'}'            
        }
        
        for char in s:
            if char in mapping.keys():
                stack.append(mapping[char])
            elif not stack or stack[-1]!=char:
                return False
            else:
                stack.pop()
        
        return len(stack)==0
        
        
test = Solution()
print(test.checkvalid('(sdsd)'))


## Balanced Brackets

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def isBalanced(base_string):
    memo = {')': '(', '}': '{', ']': '['}
    stack = [0]
    for character in base_string:
        if character in memo:
            if stack.pop() != memo[character]:
                return False
        else:
            stack.append(character)
    return stack == [0]


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
    s1 = "{[(])}"
    expected_1 = False
    output_1 = isBalanced(s1)
    check(expected_1, output_1)

    s2 = "{{[[(())]]}}"
    expected_2 = True
    output_2 = isBalanced(s2)
    check(expected_2, output_2)

  # Add your own test cases here
  