# 내 코드
def solution(brown, yellow):
    answer = []

    for i in range(1, (yellow + 1)) :
      if yellow % i == 0 :
        x = max(((yellow // i) + 2), (i + 2))
        y = min(((yellow // i) + 2), (i + 2))
        if (x + y - 2) * 2 == brown :
          answer.extend([x, y])
          return answer
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# 다른 코드
import math
def solution(brown, yellow):
    ans=((brown-4)+math.sqrt((brown-4)**2-16*yellow))//4
    return [ans+2,yellow//ans+2]
  
