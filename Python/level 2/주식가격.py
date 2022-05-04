# 내 코드
def solution(prices):
    answer = [0 for i in range(len(prices))]

    for i in range(len(prices)) :
      for j in range((i + 1), len(prices)) :
        answer[i] += 1
        if prices[i] > prices[j] :
          break

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# 다른 코드
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
