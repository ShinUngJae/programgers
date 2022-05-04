# 내 코드
from functools import reduce

def solution(n) :
    answer = []
    triangle = [[0 for i in range(j + 1)] for j in range(n)]
    a, b, c = 0, 0, 0
    num = int(n * (n + 1) / 2)

    for i in range(1, (num + 1)) :
  
      triangle[a][b] = i
      if c == 0 :
        if (a == (n - 1)) or (triangle[a + 1][b] != 0) :
          c = 1
          b += 1
        else :
          a += 1

      elif c == 1 :
        if (b == (n - 1)) or (triangle[a][b + 1] != 0) :
          c = 2
          a -= 1
          b -= 1
        else :
          b += 1

      elif c == 2 :
        if (triangle[a - 1][b - 1] != 0) :
          c = 0
          a += 1
        else :
          a -= 1
          b -= 1

    answer = reduce(lambda x, y : x + y, triangle)

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# 다른 코드
def solution(n):
    dx=[0,1,-1];dy=[1,0,-1]
    b=[[0]*i for i in range(1,n+1)]
    x,y=0,0;num=1;d=0
    while num<=(n+1)*n//2:
        b[y][x]=num
        ny=y+dy[d];nx=x+dx[d];num+=1
        if 0<=ny<n and 0<=nx<=ny and b[ny][nx]==0:y,x=ny,nx
        else:d=(d+1)%3;y+=dy[d];x+=dx[d]
    return sum(b,[])
