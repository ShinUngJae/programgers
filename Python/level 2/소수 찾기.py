# 내 코드

from itertools import permutations

def aristo(num) :
  prime_list = [True] * (num + 1)
  prime_list[0], prime_list[1] = False, False

  for i in range(2, int(num ** 0.5) + 1) :
    if prime_list[i] == True :
      for j in range(i * 2, (num + 1), i) :
        prime_list[j] = False
  
  return prime_list


def solution(numbers) :
    num_list = list(map(str, numbers))
    num_list.sort(reverse = True)
    max_num = int(''.join(num_list))

    prime_list = aristo(max_num)
    answer = 0

    for i in range(1, len(num_list) + 1) :
      permu_list = list(permutations(num_list, i))
      temp_list = []
      tmp = ''
      for j in permu_list :
        for k in j :
          tmp += k
        temp_list.append(tmp)
        tmp = ''

      for m in temp_list :
        if prime_list[int(m)] == True :
          answer += 1
          prime_list[int(m)] = False   

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
