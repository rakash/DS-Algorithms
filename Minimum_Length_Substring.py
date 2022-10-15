# 3.3 Minimum Length Substrings

def min_length_substring(s, t):
  res = []
  for i in range(len(t)):
    flag = -1
    for c in [pos for (pos, item) in enumerate(s) if item == t[i]]:
      if c is None:
        return -1
      if c not in res:
        flag = 1
        res.append(int(c))
    if flag==-1:
      return -1
  return max(res)-min(res)+1

s1 = "dcbefebce"
t1 = "fd"
expected_1 = 5
print(min_length_substring(s1, t1))

s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
t2 = "cbccfafebccdccebdd"
expected_2 = -1
print(min_length_substring(s2, t2))
