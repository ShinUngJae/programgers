# 내 코드
def solution(arr1, arr2):
    answer = arr1.copy()
    for i in range(len(arr1)) :
      for j in range(len(arr1[i])) :
        answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def sumMatrix(A,B):
  answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
  return answer
  
  
  
  










def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]
