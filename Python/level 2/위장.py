# 내 코드

from collections import Counter

def solution(clothes):
  
    answer = 1
    types = []
    for i in clothes :
      types.append(i[1])
    types2 = list(set(types))

    clothes_counter = Counter(types)

    temp = [(j + 1) for j in clothes_counter.values()]
    for k in temp :
      answer *= k

    return answer - 1
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# 다른 코드
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
  
# reduce(함수, 리스트, 초기값)
# 초기값부터 시작하여 리스트의 원소들을 연속으로 함수에 넣는다. 
  
