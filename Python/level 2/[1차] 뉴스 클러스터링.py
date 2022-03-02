# 내 코드

from collections import Counter

def counter_list(string) :
  string_2_list = []
  for i in range(len(string) - 1) :
    if string[i : i + 2].isalpha() :
      temp = string[i : i + 2].lower()
      string_2_list.append(temp)
  
  counter_list = Counter(string_2_list)

  return counter_list


def Jaccard(list1, list2) :
  intersection_count = sum(dict(list1 & list2).values())
  union_count = sum(dict(list1 | list2).values())
  if union_count == 0 :
    jaccard = 1
  else :
    jaccard = intersection_count / union_count
  
  return jaccard


def solution(str1, str2) :
    c1 = counter_list(str1)
    c2 = counter_list(str2)

    jaccard = Jaccard(c1, c2)
    answer = int(65536 * jaccard)
  
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
# re.findall : 문자열 중 패턴과 일치되는 모든 부분을 찾음
# + : 1번 이상 반복
# * : 0번 이상 반복
# ? : 0~1번 반복
