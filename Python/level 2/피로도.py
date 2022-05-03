# 내 코드
from itertools import permutations
from collections import deque

def solution(k, dungeons) :
    answer = 0
    temp = 0
    k2 = k
    num = len(dungeons)
    per = deque(permutations(range(num)))

    while (answer != num) and (per) :
      p = per.popleft()
      for i in range(len(p)) :
        if (k2 >= max(dungeons[p[i]][0], dungeons[p[i]][1])) :
          k2 -= dungeons[p[i]][1]
          temp += 1
        else :
          break
      if temp > answer :
        answer = temp
      temp = 0
      k2 = k

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  
  
  
  
# 다른 코드
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
 
