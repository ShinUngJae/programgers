# 내 코드 : 효율성 테스트 불합
# 웬만하면 numpy pandas 사용 X 

import pandas as pd
import re

def solution(info, query) :

    answer = []
    recruit = [i for i in range(len(info))]

    for i in range(len(info)) :
      temp = info[i].split()
      temp[4] = int(temp[4])
      recruit[i] = temp

    recruit2 = pd.DataFrame(recruit, columns = ['Tool', 'Group', 'Career', 'Food', 'Score'])

    for j in range(len(query)) :
      temp = re.split(' ', query[j])
      while 'and' in temp :
          temp.remove('and')
      temp[4] = int(temp[4])
      temp

      if temp[0] == '-' :
        r1 = recruit2.copy()
      else :
        r1 = recruit2.loc[recruit2['Tool'] == temp[0], :]

      if temp[1] == '-' :
        r2 = r1.copy()
      else :
        r2 = r1.loc[r1['Group'] == temp[1], :]

      if temp[2] == '-' :
        r3 = r2.copy()
      else :
        r3 = r2.loc[r2['Career'] == temp[2], :]

      if temp[3] == '-' :
        r4 = r3.copy()
      else :
        r4 = r3.loc[r3['Food'] == temp[3], :]

      r5 = r4.loc[r4['Score'] >= temp[4], :]

      answer.append(len(r5))

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# 다른 코드
import re

def solution(info, query) :
    data = dict()
    for a in ['cpp', 'java', 'python', '-'] :
      for b in ['backend', 'frontend', '-'] :
        for c in ['junior', 'senior', '-'] :
          for d in ['chicken', 'pizza', '-'] :
            data.setdefault((a, b, c, d), [])
    
    for i in info :
      i = i.split()
      for a in [i[0], '-'] :
        for b in [i[1], '-'] :
          for c in [i[2], '-'] :
            for d in [i[3], '-'] :
              data[(a, b, c, d)].append(int(i[4]))
    
    for k in data :
      data[k].sort()

    answer = []
    for q in query :
      q = re.split(' ', q)
      while 'and' in q :
        q.remove('and')
    
      pool = data[(q[0], q[1], q[2], q[3])]
      find = int(q[4])
      l = 0
      r = len(pool)
      mid = 0
      while l < r :
        mid = (r + l) // 2
        if pool[mid] >= find :
          r = mid
        else :
          l = mid + 1
      answer.append(len(pool) - l)

    return answer
  
# setdefault
# key 가 딕셔너리에 있으면 해당 값을 돌려줍니다.
# 그렇지 않으면, default 값을 갖는 key 를 삽입한 후 default 를 돌려줍니다.
  
  
  
