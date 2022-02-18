# 내 코드
def solution(s, n) :
    answer = ''
    for i in s :
      if i.isupper() :
        if ord(i) + n > ord('Z') :
          answer += chr(ord(i) + n - 26)
        else :
          answer += chr(ord(i) + n)
      elif i.islower() :
        if ord(i) + n > ord('z') :
          answer += chr(ord(i) + n - 26)
        else :
          answer += chr(ord(i) + n)
      else :
        answer += ' '
    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
