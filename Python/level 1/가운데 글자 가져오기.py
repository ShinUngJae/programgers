# 내 코드
def solution(s) :
    if len(s) % 2 == 0 :
      answer = s[(len(s) // 2) - 1] + s[(len(s) // 2)]
    else :
      answer = s[(len(s) // 2)]
    return answer
  
  
  
  
  
  
  
  
  
def string_middle(str):

    return str[((len(str) - 1) // 2) : (len(str) // 2 + 1)] 
