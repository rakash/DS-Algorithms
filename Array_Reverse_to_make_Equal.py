# Array - Reverse to make Equal

def are_they_equal(array_a, array_b):
      # Write your code here
  x = int(len(array_a))
  array_a.sort()
  array_b.sort()
  for i in range(x):
    if array_a[i] != array_b[i]:
      return False
  return True

def are_they_equal_another_method(array_a, array_b):
    n = len(array_a)
    bag1 = {}
    bag2 = {}
  
    for i in range(n):
        if array_a[i] not in bag1:
            bag1[array_a[i]] = 1
        else:
            bag1[array_a[i]] += 1
        print(bag1)
      
        if array_b[i] not in bag2:
            bag2[array_b[i]] = 1
        else:
            bag2[array_b[i]] += 1
        print(bag2)
    return bag1 == bag2

a, b = [1, 2, 3, 4], [4, 3, 2, 1]

print(are_they_equal(a,b))
print(are_they_equal_another_method(a,b))