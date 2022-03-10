# u, v 분리
def balance(p) :
  u = ''
  for i in range(len(p)) :
    u += p[i]
    if u.count('(') == u.count(')') :
      break
  v = p[i + 1 : ]
  return u, v

# 올바른 괄호 문자열 판별
def correct(p) :
  stack = []
  for i in p :
    if i == '(' :
      stack.append(i)
    else :
      if len(stack) == 0 :
        return False
      else :
        stack.pop()
  if len(stack) > 0 :
    return False
  else:
    return True

# 전체 로직
def parentheses(p) :
  result = ''
  if p == '' :
    return ''
  u, v = balance(p)
  if correct(u) :
    return u + parentheses(v)
  else :
    temp = '(' 
    temp += parentheses(v) + ')'
    u = u[1 : len(u) - 1]
    for i in u :
      if i == '(' :
        temp += ')'
      else :
        temp += '('
  result += temp
  return result

# 전체 소스 코드
def solution(p) :
    answer = ''
    if correct(p) :
      return p
    answer = parentheses(p)
    return answer
  
  
  
 
  
  
  
  
  
  
  
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
