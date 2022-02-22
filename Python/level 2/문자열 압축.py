# 내 코드
def solution(s) :
    answer = ['' for _ in range(0, len(s) + 1)]
    for i in range(1, (len(s) + 1)) :
      num = 1
      for j in range(0, len(s), i) :
        if j == 0 :
          ab_letter = s[0 : i]
          letter = ab_letter
        else :
          letter = s[j : (i + j)]
          if (ab_letter == letter) :
            num += 1
          else :
            if num > 1 :
              answer[i] += str(num)
            answer[i] += ab_letter
            ab_letter = letter
            num = 1
      if num > 1 :
        answer[i] += str(num)
        answer[i] += ab_letter
      else :
        answer[i] += letter

    answer2 = []
    for i in answer :
      answer2.append(len(i))
    answer3 = answer2[1 : ]
    length = min(answer3)
    return length
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def solution(s):
    answer = len(s)
    for x in range(1, int(len(s)/2)+1):
        d = 0
        comp = ''
        c = 1
        for i in range(0, len(s), x):
            temp = s[i:i+x]
            if comp == temp:
                c += 1
            elif comp != temp:
                d += len(temp)
                if c > 1:
                    d += len("{}".format(c))
                c = 1
                comp = temp
        if c > 1:
            d += len("{}".format(c))
        answer = min(answer, d)
    return answer
