# stack 사용법

def solution(s) :

    t = []

    for i in s :
      if (len(t) > 0) and (t[-1] == i) :
        t.pop()
      else :
        t.append(i)

    if len(t) == 0 :
      answer = 1
    else :
      answer = 0

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
