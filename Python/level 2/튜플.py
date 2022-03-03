# 내 코드
import re

def solution(s):
    s = s[1 : len(s) - 1]
    s = re.findall('\{.*?\}', s)

    temp_list = [[] for i in range(len(s))]

    for i in range(len(s)) :
      temp = ''
      for j in s[i] :
        if j.isdigit() :
          temp += j
        else :
          if temp != '' :
            temp_list[i].append(int(temp))
            temp = ''

    num_list = [[] for i in range(len(s))]

    for i in temp_list :
      num_list[len(i) - 1].extend(i)

    answer = []
    for i in range(len(num_list)) :
      j = list(set(num_list[i]) - set(answer))
      answer.extend(j)

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
import re
from collections import Counter

  def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
  
  
  
  
  
  
