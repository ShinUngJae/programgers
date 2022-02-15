# 내 코드

def solution(answers) :
    ans1 = 0
    ans2 = 0
    ans3 = 0
    answer = []

    for i in range(1, len(answers) + 1) :
  
        stu1 = [5, 1, 2, 3, 4]
        stu2 = [5, 2, 1, 2, 3, 2, 4, 2]
        stu3 = [5, 3, 3, 1, 1, 2, 2, 4, 4, 5]

        loop1 = i % 5
        loop2 = i % 8
        loop3 = i % 10

        if stu1[loop1] == answers[i - 1] :
            ans1 += 1
        if stu2[loop2] == answers[i - 1] :
            ans2 += 1
        if stu3[loop3] == answers[i - 1] :
            ans3 += 1

    ans = {1 : ans1, 2 : ans2, 3 : ans3}
    for i in ans.keys() :
        if ans[i] == max(ans.values()) :
            answer.append(i)
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
  
  
  
  
  
  
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:     # cycle를 쓰면 next로 계속 다음 숫자를 자동으로 불러와준다.
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
