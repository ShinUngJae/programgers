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
  
# heapq : 일반적인 리스트와 다르게 가지고 있는 요소를 push, pop 할때마다 자동으로 정렬
# heapq.heappop : heapq에서 가장 작은 항목을 pop하고 반환
# heapq.heappush(heap, item) : heap에 item 값을 넣는다.
  
  
  
  
  
  
  
  
  
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


# heapq.heapify : 리스트 x를 즉각적으로 heap으로 변환
