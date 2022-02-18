# 내 코드

def solution(n) :
    return [int(str(n)[i]) for i in range((len(str(n)) - 1), -1, -1)]
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
