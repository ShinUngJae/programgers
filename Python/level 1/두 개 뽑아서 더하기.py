# 내 코드
from itertools import combinations

def solution(numbers) :
    sum_list = list(combinations(numbers, 2))
    answer = []
    for i in sum_list :
      print(i)
      if sum(i) not in answer :
        answer.append(sum(i))
    answer.sort()
    return answer
