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
  
# deque 사용 이유 : 시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는 데 최적화된 연산 속도를 제공
# deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
# deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
# deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
# deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
# deque.remove(item): item을 데크에서 찾아 삭제한다.
# deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽). 
  

    
    
# stack : 책을 쌓는 것처럼 차곡차곡 쌓아 올린 형태의 자료구조
# 스택은 시간 순서에 따라 자료가 쌓여서 가장 마지막에 삽입된 자료가 가장 먼저 삭제
# 예 : 웹 브라우저 방문기록 (뒤로 가기) : 가장 나중에 열린 페이지부터 다시 보여준다


# queue : 한쪽 끝에서 삽입 작업이, 다른 쪽 끝에서 삭제 작업이 양쪽으로 이루어진다
# 큐는 주로 데이터가 입력된 시간 순서대로 처리해야 할 필요가 있는 상황에 이용
# 예 : 은행 업무, 프린터의 인쇄 대기열
