# 내 코드
def solution(x):
    a = sum(int(i) for i in str(x))
    answer = True if x % a == 0 else False
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  def Harshad(n):
    return not( n % sum([int(x) for x in str(n)]))
 
