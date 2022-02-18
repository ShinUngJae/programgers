# 내 코드
from collections import Counter

def solution(n) :
    divisor_list = []
    m = 2
    while n > 1 :
      if n % m == 0 :
        divisor_list.append(m)
        n = (n // m)
        m = 2
      else :
        m += 1

    divisor_counter = Counter(divisor_list)
    answer = 1
    for p, q in divisor_counter.items() :
      answer *= (p ** (q + 1) - 1) / (p - 1)
    
    if n == 0 :
      answer = 0
    
    return int(answer)
  
  
  
  
  
  
  
  
  
  
  
  
  
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
