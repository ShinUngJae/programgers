# 내 코드

def solution(places) :
    answer = [1 for i in range(5)]
    for k in range(5) :
      waiting = [[j for j in i] for i in places[k]]
      covid = 1
      for i in range(5) :
        for j in range(5) :
          if waiting[i][j] == 'P' :
            temp_list1 = []
            if i > 0 :
              temp_list1.append(waiting[i - 1][j])
            if i < 4 :
              temp_list1.append(waiting[i + 1][j])
            if j > 0 :
              temp_list1.append(waiting[i][j - 1])
            if j < 4 :
              temp_list1.append(waiting[i][j + 1])
            if 'P' in temp_list1 :
              answer[k] = 0
              print('temp1', answer)
              break
            temp_list2 = []
            if j > 1 :
              temp_list2.append(set(waiting[i][j - 2 : j]))
            if j < 3 :
              temp_list2.append(set(waiting[i][j + 1 : j + 3]))
            if i > 1 :
              temp_list2.append(set(waiting[i - 1][j] + waiting[i - 2][j]))
            if i < 3 :
              temp_list2.append(set(waiting[i + 1][j] + waiting[i + 2][j]))
            if {'O', 'P'} in temp_list2 :
              answer[k] = 0
              print('temp2', answer)
              break
            temp_list3 = []
            if i > 0 :
              if j > 0 :
                temp_list3.append(set(waiting[i - 1][j - 1] + waiting[i][j - 1]))
                temp_list3.append(set(waiting[i - 1][j - 1] + waiting[i - 1][j]))
              if j < 4 :
                temp_list3.append(set(waiting[i - 1][j + 1] + waiting[i][j + 1]))
                temp_list3.append(set(waiting[i - 1][j + 1] + waiting[i - 1][j]))
            if i < 4 :
              if j > 0 :
                temp_list3.append(set(waiting[i + 1][j - 1] + waiting[i][j - 1]))
                temp_list3.append(set(waiting[i + 1][j - 1] + waiting[i + 1][j]))
              if j < 4 :
                temp_list3.append(set(waiting[i + 1][j + 1] + waiting[i][j + 1]))
                temp_list3.append(set(waiting[i + 1][j + 1] + waiting[i + 1][j]))   
            if {'O', 'P'} in temp_list3 :
              answer[k] = 0
              print('temp3', answer)
              break
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# BFS
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우

def bfs(place, i, j) :
  visit = [[0] * 5 for _ in range(5)]
  q = deque()
  q.append((i, j, 0))
  visit[i][j] = 1

  while q :
    x, y, dist = q.popleft()
    if 0 < dist < 3 and place[x][y] == 'P' :
      return False
    if dist > 2 :
      break # 거리가 3 부터는 탐색 중단(거리두기를 잘 지킨 경우이기 때문에)
    for k in range(4) :
      nx, ny, nd = x + dx[k], y + dy[k], dist + 1
      if 0 <= nx < 5 and 0 <= ny < 5 :
        if place[nx][ny] != 'X' and not visit[nx][ny] : # 파티션이 있는 경우만 아니면 이동가능
           q.append((nx, ny, nd))
           visit[nx][ny] = 1
  return True


def solution(places) :
  answer = []

  for place in places :
    chk = 0
    for i in range(5) :
      for j in range(5) :
        if place[i][j] == 'P' :
          if not bfs(place, i, j) :
            answer.append(0)
            chk = 1
            break
      if chk :
        break
    else :
      answer.append(1)
    
  return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
