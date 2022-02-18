# 내 코드
def solution(n) :
    a = []
    for i in str(int(n)) :
      a.append(i)
    a.sort(reverse = True)
    answer = ''
    for j in a :
      answer += j

    answer2  = int(answer)
    return answer2
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
