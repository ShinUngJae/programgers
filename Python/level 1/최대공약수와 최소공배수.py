# 내 코드
def solution(n, m):
    divisor_list = [1]
    for i in range(2, (max(n, m) // 2 + 1)) :
      if (n % i == 0) and (m % i == 0) :
        divisor_list.append(i)
    answer = []
    answer.append(max(divisor_list))
    answer.append(answer[0] * (n // answer[0]) * (m // answer[0]))
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
  
  
  
  
  
  

  
  
  
  
  
  
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]
