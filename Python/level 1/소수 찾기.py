# 내 코드
def solution(n) :
    aristo = [True] * (n + 1)
    aristo[0], aristo[1] = False, False
    for i in range(2, (int(n ** 0.5) + 1)) :
      if aristo[i] == True :
        for j in range(i + i, n + 1, i) :
          aristo[j] = False
    answer = sum(aristo)
    return answer
  
  
  
  
  
  
  
  
  
def solution(n) :
  
    num = set(range(2, n + 1))

    for i in range(2, n + 1) :
        if i in num:
            num -= set(range(2 * i, n + 1, i))
            
    return len(num)
