# 내 코드

def solution(s) :
    answer_list = []

    for i in s :
      answer_list.append(i)

    answer_list.sort(reverse = True)

    answer = ''
    for j in answer_list :
      answer += j
    return answer
  
  
  
  
  
  
  
  
  
def solution(s):
    return ''.join(sorted(s, reverse=True))
  
  
  
  
  
  
  
  
  
  def solution(s):
    s = list(s)
    s.sort(reverse = True)
    answer = ""
    for i in s:
        answer = answer + i
    return answer
