# Dynamic Arrays

import ctypes

class DynamicArray():
    
    def __init__(self):
        self.n = 0 # By default
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
    #Length method
    def __len__(self):
      #It will return number of elements in the array
        return self.n
    
    def __getitem__(self, k):
          #it will return the elements at the index k
        if not 0 <= k < self.n:
            return IndexError('k is out of bounds')
        return self.A[k]
    
    def append(self, element):
       #checking the capacity
        if self.n == self.capacity:
            #double the capacity for the new array i.e
            self.resize(2*self.capacity) # resize is the method that is defined later
    # Set the n indexes of array A to elements
        print('append length')
        print(self.n)
        self.A[self.n] = element
        self.n += 1
        
    def resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            print('FOR')
            print(self.n)
            print('resize length')
            print(self.n)
            B[k]= self.A[k]
        self.A = B
        self.capacity = new_cap
        print('capacity')
        print(self.capacity)
        
    def make_array(self, new_cap):
        return(new_cap * ctypes.py_object)()
    
try_it = DynamicArray()
#print(len(try_it))