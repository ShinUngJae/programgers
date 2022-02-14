# 내 코드
def solution(absolutes, signs) :
    answer = 0
    for i, j in zip(absolutes, signs) :
      if j == True :
        answer += i
      else :
        answer -= i
    return answer
  
  
  
  
  
  
  
  
  

def solution(absolutes, signs) :
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
