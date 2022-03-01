# 내 코드

def solution(rows, columns, queries) :
    matrix = [[j for j in range(columns * (i - 1) + 1, columns * i + 1)] for i in range(1, rows + 1)]
    matrix2 = matrix.copy()
    matrix_T = list(map(list, zip(*matrix.copy()))

    answer_num = []
    answer = []
    for q in queries :

      answer_num.extend(matrix[(q[0] - 1)][(q[1] - 1) : (q[3] - 1)])
      answer_num.extend(matrix[(q[2] - 1)][(q[1]) : (q[3])])
      answer_num.extend(matrix_T[(q[3] - 1)][(q[0] - 1) : (q[2] - 1)])
      answer_num.extend(matrix_T[(q[1] - 1)][(q[0]) : (q[2])])

      matrix2[(q[0] - 1)][(q[1]) : (q[3])] = matrix[(q[0] - 1)][(q[1] - 1) : (q[3] - 1)]
      matrix2[(q[2] - 1)][(q[1] - 1) : (q[3] - 1)] = matrix[(q[2] - 1)][(q[1]) : (q[3])]

      matrix2 = list(map(list, zip(*matrix2)))


      matrix2[(q[3] - 1)][(q[0]) : (q[2])] = matrix_T[(q[3] - 1)][(q[0] - 1) : (q[2] - 1)]
      matrix2[(q[1] - 1)][(q[0] - 1) : (q[2] - 1)] = matrix_T[(q[1] - 1)][(q[0]) : (q[2])]

      matrix2 = list(map(list, zip(*matrix2)))

      answer.append(min(answer_num))
      answer_num = []
      matrix = matrix2.copy()
      matrix_T = list(map(list, zip(*matrix.copy())))

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
# deque를 이용한 풀이
from collections import deque
                    
def solution(rows, columns, queries) :
    arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]
    answer, result = deque(), []
    for i in queries:
        a,b,c,d = i[0]-1, i[1]-1, i[2]-1, i[3]-1
        for x in range(d-b):
            answer.append(arr[a][b+x])
        for y in range(c-a):
            answer.append(arr[a+y][d])
        for z in range(d-b):
            answer.append(arr[c][d-z])
        for k in range(c-a):
            answer.append(arr[c-k][b])
        answer.rotate(1)
        result.append(min(answer))
        for x in range(d-b):
            arr[a][b+x] = answer[0]
            answer.popleft()
        for y in range(c-a):
            arr[a+y][d] = answer[0]
            answer.popleft()
        for z in range(d-b):
            arr[c][d-z] = answer[0]
            answer.popleft()
        for k in range(c-a):
            arr[c-k][b] = answer[0]
            answer.popleft()
    return result
  
# deque.rotate(k) : k만큼 리스트 값이 앞으로 옮겨진다. 맨 뒤의 원소는 앞으로 보내진다.
# deque.popleft() : 가장 왼쪽의 값이 빠진다.
  
  
  
  
  
  
  
  
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
def solution(rows, columns, queries):
    answer = []
    table = []
    for r in range(rows):
        table.append([a for a in range(r*columns+1, (r+1)*columns+1)])
    
    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    
    return answer
  
  
  
