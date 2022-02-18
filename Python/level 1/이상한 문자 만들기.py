# 내 코드

def solution(s) :
    answer = ''
    letter = 0
    for i in s :
      if i.isalpha() :
        if letter % 2 == 0 :
          answer += i.upper()
        else :
          answer += i.lower()
        letter += 1
      else :
        answer += ' '
        letter = 0

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def solution(s):
    answer = ''
    for word in s.split(" "):
        n = ''
        for i in range(len(word)):
            if i%2 == 0 :
                n += word[i].upper()
            else :
                n += word[i].lower()
        answer += (n + " ")
    return answer[0:-1]
