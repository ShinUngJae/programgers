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
  
  
  
