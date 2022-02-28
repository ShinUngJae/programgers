# 내 코드

import math

def solution(progresses, speeds) :
    days = []
    answer = []

    for u, v in zip(progresses, speeds) :
      days.append(math.ceil((100 - u) / v))

    a = days[0]
    count = 0

    for i in days :
      if max(a, i) == a :
        count += 1
      else :
        answer.append(count)
        count = 1
        a = i

    answer.append(count)

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  def solution(progresses, speeds) :
    Q=[]
    for p, s in zip(progresses, speeds) :
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s) :
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]
  
  
  
  
  
  
  
  
  
