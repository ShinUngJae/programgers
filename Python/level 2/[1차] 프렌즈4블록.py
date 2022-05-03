# 내 코드
from functools import reduce

def solution(m, n, board) :
    temp = 1
    answer = 0
    removed = [[False for i in range(n)] for j in range(m)]
    
    while temp > 0 :
      temp = 0
      board2 = ['' for i in range(n)]
      for i in range(m - 1) :
        for j in range(n - 1) :
          block = board[i][j]
          if (board[i][j + 1] == block) and (board[i + 1][j] == block) and (board[i + 1][j + 1] == block) and (block != '4'):
            removed[i][j], removed[i][j + 1], removed[i + 1][j], removed[i + 1][j + 1] = True, True, True, True
      removed2 = list(reduce(lambda x, y: x + y, removed))
      temp = sum(removed2)
      answer += temp
      for j in range(m) :
        for i in range(n) :
          if not removed[j][i] and board[j][i] != '4':
            board2[i] += board[j][i]

      for i in range(n) :
        board2[i] = board2[i].rjust(m, '4')
      
      board = list(map(list, zip(*board2)))
      removed = [[False for i in range(n)] for j in range(m)]

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# 다른 코드
x = board
x2 =[]

for i in x: 
    x1 = []
    for i2 in i:
        x1.append(i2)
    x2.append(x1)

point = 1
while point != 0:
    list = []
    point = 0
    for i in range(m - 1):
        for j in range(n - 1):
            if x2[i][j] == x2[i][j + 1] == x2[i + 1][j] == x2[i + 1][j + 1] != '팡!':
                list.append([i, j])
                point += 1

    for i2 in list:
        i, j = i2[0], i2[1]
        x2[i][j], x2[i][j + 1], x2[i + 1][j], x2[i + 1][j + 1] = '팡!', '팡!', '팡!', '팡!'

    for i3 in range(m):
        for i in range(m - 1):
            for j in range(n):
                if x2[i + 1][j] == '팡!':
                    x2[i + 1][j], x2[i][j] = x2[i][j], '팡!'

cnt = 0
for i in x2:
    cnt += i.count('팡!')
