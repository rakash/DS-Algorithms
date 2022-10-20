# 6 - Binary Search - Revenue Milestones

def getMilestoneDays(revenues, milestones):
  m = 0
  mppng = {x:i for i,x in enumerate(milestones)}
  milestones.sort()
  LM = len(milestones)
  prfxsm = 0
  ret = [0 for _ in range(LM)]
  for i, x in enumerate(revenues):
    prfxsm += x
    while m < LM and prfxsm >= milestones[m]:
      ret[mppng[milestones[m]]] = i+1
      m += 1
    if m == LM:
      break
  return ret

revenues = [100, 200, 300, 400, 500]
milestones = [300, 800, 1000, 1400]
print(getMilestoneDays(revenues, milestones))

revenues_2 = [700, 800, 600, 400, 600, 700]
milestones_2 = [3100, 2200, 800, 2100, 1000]
print(getMilestoneDays(revenues_2, milestones_2))