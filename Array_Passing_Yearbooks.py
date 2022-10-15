## 2.2 - Array - Passing Yearbooks

def findSignatureCounts(arr):
  L = len(arr)
  res = [0] * L
  print(res)
  # set of visited students
  visited = set()
  print('visited')
  print(visited)
  for i in range(len(arr)):
    if i not in visited:
      j = i
      # the students of the same group as student i
      group = set([i])
      # keep passing the yearbook until it goes back to i
      while arr[j]-1 != i:
        j = arr[j]-1
        group.add(j)
      # update the visited set
      visited.update(group)
      for k in group:
        res[k] = len(group)
  return res

arr_1 = [1, 2]
#expected_1 = [1, 1]
print(findSignatureCounts(arr_1))