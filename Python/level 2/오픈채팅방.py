# 내 코드
def solution(record):
    answer = []
    record2 = [i.split() for i in record]
    for i in record2 :
      if len(i) == 2 :
        i.append('')

    user = {}
    for i in record2 :
      if i[0] != 'Leave' :
        user[i[1]] = i[2]

    answer = []
    for i in record2 :
      if i[0] == 'Enter' :
        answer.append('%s님이 들어왔습니다.' % user[i[1]])
      elif i[0] == 'Leave' :
        answer.append('%s님이 나갔습니다.' % user[i[1]]) 
    
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
