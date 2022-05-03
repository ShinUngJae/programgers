# 내 코드

def solution(numbers):
    answer = []
    for i in numbers :
      num = str(bin(i))[2 :]

      if '0' not in num :
        num = '10' + num[1 :]
      elif num[-1] == '0' :
        num = num[: (len(num) - 1)] + '1'
      else :
        for i in range((len(num) - 1), -1, -1) :
          if num[i] == '0' :
            num = num[: i] + '10' + num[(i + 2) :]
            break

      answer.append(int(num, 2))

    return answer
