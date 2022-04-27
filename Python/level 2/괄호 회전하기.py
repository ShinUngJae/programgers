# 내 코드
from collections import Counter

def solution(s) :
    answer = 0
    num = len(s)

    if len(s) % 2 == 1 :
      return 0

    ss = Counter(s)
    if (ss['['] != ss[']']) or (ss['{'] != ss['}']) or (ss['('] != ss[')']) :
      return 0

    for _ in range(num) :
      s2 = s[1 :] + s[0]

      temp = ''
      temp3 = True
      for i in range(num) :
        temp += s2[i]
        temp2 = Counter(temp)

        if (i < (num - 1)) :
          if (s2[i] == '[') and (s2[i + 1] in ['}', ')']) :
            temp3 = False
            break
          if (s2[i] == '{') and (s2[i + 1] in [']', ')']) :
            temp3 = False
            break
          if (s2[i] == '(') and (s2[i + 1] in [']', '}']) :
            temp3 = False
            break

        if (temp2['['] < temp2[']']) or (temp2['{'] < temp2['}']) or (temp2['('] < temp2[')']) :
          temp3 = False
          break
      if temp3 == True :
        answer += 1
      s = s2

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# 다른 코드
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer
