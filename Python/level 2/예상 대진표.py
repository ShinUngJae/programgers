# 내 코드

import math

def solution(n,a,b):
    answer = 1
    while True :
      a = math.ceil(a / 2)
      b = math.ceil(b / 2)
      if (a == b) :
        return answer
      answer += 1
