import heapq as hq

def solution(scoville, K) :
    answer = 0
    scoville.sort()
    while len(scoville) > 1 :

      a = hq.heappop(scoville)
      b = hq.heappop(scoville)
      if a >= K :
        break
      hq.heappush(scoville, a + b * 2)
      answer += 1

    if ((len(scoville) == 1) and (scoville[0] < K)) :
      answer = -1
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
