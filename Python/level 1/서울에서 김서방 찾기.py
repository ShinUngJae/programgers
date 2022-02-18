# 내 코드
def solution(seoul) :
    for i in range(len(seoul)) :
      if seoul[i] == 'Kim' :
        answer = '김서방은 ' + str(i) + '에 있다'
    return answer
  
  
  
  
  
  
  
  
  
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
