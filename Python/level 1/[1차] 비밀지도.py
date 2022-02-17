# 내 코드
def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    for i in range(n) :
      a = bin(arr1[i])
      a = a[2 :]
      b = bin(arr2[i])
      b = b[2 :]
      if len(a) < n :
        map1.append('0' * (n - len(a)) + a)
      else :
        map1.append(a)
      if len(b) < n :
        map2.append('0' * (n - len(b)) + b)
      else :
        map2.append(b)

    map = ['' for _ in range(n)]
    for j in range(n) :
      for p in range(n) :
        if (map1[j][p] == '1') or (map2[j][p] == '1') :
          map[j] += '1'
        else :
          map[j] += '0'

    answer = ['' for _ in range(n)]
    for k in range(n) :
      for m in range(n) :
        if map[k][m] == '1' :
          answer[k] += '#'
        else :
          answer[k] += ' '
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def solution(n, arr1, arr2) :
    answer = []
    for i, j in zip(arr1,arr2) :
        a12 = str(bin(i|j)[2 :])
        a12=a12.rjust(n, '0')
        a12=a12.replace('1', '#')
        a12=a12.replace('0', ' ')
        answer.append(a12)
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
import re

def solution(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer
