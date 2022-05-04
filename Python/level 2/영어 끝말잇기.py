# 내 코드
def solution(n, words):
    answer = [0, 0]

    letter = ''
    words_set = []
    for i in words :

      if answer[0] in [0, n] :
        answer[0] = 1
        answer[1] += 1
      else :
        answer[0] += 1

      if ((len(letter) == 0) or (letter[-1] == i[0])) and (i not in words_set) :
        letter = i
        words_set.append(i)
        print(i, words_set)
      else :
        break
    else :
      answer = [0, 0]

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# 다른 코드
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
