import math

def solution(w, h) :
    answer = w * h - (w + h + math.gcd(w, h))
    return answer
  
  
# 참고 
# math.lcm : 최소공배수
# math.gcd : 최대공약수
