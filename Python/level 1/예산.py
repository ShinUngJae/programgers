# 내 코드
def solution(d, budget) :
  d.sort()
  i = 0
  answer = 0
  if sum(d) <= budget :
    i = len(d)
  else :
    while (budget >= 0) :
      budget -= d[i]
      i += 1
    i -= 1
  return i
















def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
