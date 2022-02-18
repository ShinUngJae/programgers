# 내 코드

def solution(n) :
    answer = ''
    for i in range(1, n + 1) :
      if i % 2 == 1 :
        answer += '수'
      else :
        answer += '박'
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def water_melon(n) :
    return ("수박" * n)[0 : n]
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def solution(n) :
    return "".join(["수박"[i%2] for i in range(n)])
