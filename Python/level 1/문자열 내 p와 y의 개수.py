# 내 코드

def solution(s) :
    ss = s.lower()
    
    if ss.count('p') == ss.count('y') :
      answer = True
    else :
      answer = False

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
from collections import Counter
def numPY(s) :

    c = Counter(s.lower())
    return c['y'] == c['p'] 
