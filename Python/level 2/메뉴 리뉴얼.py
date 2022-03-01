from itertools import combinations
from collections import Counter

def solution(orders, course) :

    answer = []

    for num in course :
      combi_list = []
      for order in orders :
        temp = combinations(sorted(order), num)
        combi_list += temp
      
      counter_list = Counter(combi_list)
      if (len(counter_list) != 0) and (max(counter_list.values()) > 1) :
        answer += [''.join(i) for i in counter_list if max(counter_list.values()) == counter_list[i]]
    
    answer.sort()

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
  
  
# collections.Counter().most_common() : 데이터의 개수가 많은 순으로 정렬된 배열을 리턴
