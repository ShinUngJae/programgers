# 내 코드

def solution(left, right) :
    answer = sum(i for i in range(left, right + 1))
    if left == 1 :
      answer -= 2
    if int(left ** 0.5) < int(right ** 0.5) :
      for i in range(int(left ** 0.5) + 1, int(right ** 0.5) + 1) :
        answer -= (i ** 2) * 2 
    return answer
  
  
  
  
  
def solution(left, right) :
    answer = 0
    for i in range(left, right + 1) :
        if int(i ** 0.5) == i ** 0.5 :
            answer -= i
        else:
            answer += i
    return answer
