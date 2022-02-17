# 내 코드
def solution(sizes) :

    for i in sizes :
      i.sort()
    
    a, b = [], []

    for j in sizes :
      a.append(j[0])
      b.append(j[1])

    answer = max(a) * max(b)
    
    return answer
  
  
  
  
  
  
  
  
  
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
