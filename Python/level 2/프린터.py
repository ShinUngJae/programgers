# 내 코드

from collections import deque

def solution(priorities, location) :
    answer = 0
    priorities_deque = deque(priorities)

    while True :

      max_index = priorities_deque.index(max(priorities_deque))
      priorities_deque.rotate(-max_index)

      location -= max_index
      if location < 0 :
        location = len(priorities_deque) + location

      if location == 0 :
        answer += 1
        return answer

      else :
        priorities_deque.popleft()
        answer += 1
        location -= 1
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
