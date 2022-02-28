# BFS
# numbers의 숫자를 더하거나 뺀 경우를 수평적으로 추가
# 결국 leaves리스트에 모든 계산 결과가 담기게 된다. 이후 target값과 비교해서 결과 출력

def solution(numbers, target) :
    answer = 0
    leaves = [0]
    for num in numbers :
      tmp = []
      for parent in leaves :
        tmp.append(parent + num)
        tmp.append(parent - num)
      leaves = tmp

    for leaf in leaves :
      if leaf == target :
        answer += 1
    return answer






# DFS
# BFS가 수평적으로 더해 한꺼번에 모든 결과값을 얻었다면, DFS를 이용할 땐 하나씩 비교
# depth 변수 값을 통해 탐색 중인 트리의 깊이를 확인
# 트리 끝에 도착했다면, number값을 모두 더한 값을 비교

answer = 0

def DFS(L, sum, numbers, target) :
      global answer
      N = len(numbers)
      if L == N :
        if target == sum :
          answer += 1
          return
      else :
        DFS(L + 1, sum + numbers[L], numbers, target)
        DFS(L + 1, sum - numbers[L], numbers, target)

def solution(numbers, target) :
      global answer
      DFS(0, 0, numbers, target)
      return answer



















def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

      
      
      
      
      
      
      
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
  
# product : 데카르트 곱



