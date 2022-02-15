from itertools import combinations

def aristo(num) :
  
  aristo = [True] * (num + 1)
  aristo[0], aristo[1] = False, False

  for i in range(2, int(num ** (1/2)) + 1) :
    if aristo[i] == True :
      for j in range(i * 2, num + 1, i) :
        aristo[j] = False
  
  return aristo

def solution(nums) :

  answer = 0
  prime_number = aristo(3000)
  combi = list(combinations(nums, 3))

  for i in combi :
    sums = sum(i)
    if prime_number[sums] :
      answer += 1

  return answer











