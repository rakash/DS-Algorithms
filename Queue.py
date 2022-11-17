class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None 
        
    def enqueue(self, value): # adds to the rear
        node = Node(value)
        if self.rear:
            self.rear.next = node 
            self.rear = node
        else:
            self.rear = node
            self.front = node
    
    def dequeue(self): # removes from the front
        if not self.front:
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        return value
    
queue = Queue()
array = [1, 2, 3, 4, 5]    
for a in array:
    queue.enqueue(a)

for _ in range(len(array)):
    print(queue.dequeue())

## Queue Removals

from collections import deque
def findPositions(arr: list, x:int):
    
    q = deque()
    for e in enumerate(arr):
        q.append(e)

    out = []         
    for _ in range(x):
        maxi = float('-inf')
        i = 0
        popli = []
        ind_to_remove = None
        while q and i < x:
            popped = q.popleft()
            if popped[1] > maxi:
                maxi = popped[1]
                ind_to_remove = popped[0]
            popli.append(popped)
            i += 1
        for t in popli:
            if t[0] != ind_to_remove:
                q.append((t[0], max(0, t[1]-1 )))
            
        out.append(ind_to_remove + 1)
    return out