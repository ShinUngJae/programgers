def solution(dartResult) :
    num_list = []
    SDT_list = []
    bonus_list = ['-' for i in range(len(dartResult))]
    num = 0
    for i in range(len(dartResult)) :
      if dartResult[i].isdigit() :
        if (dartResult[i] == '1') & (dartResult[i + 1] == '0') :
          num_list.append('10')
          num += 1
        elif (dartResult[i] == '0') & (dartResult[i - 1] == '1') :
          pass
        else :
          num_list.append(dartResult[i])
          num += 1
      elif dartResult[i].isalpha() :
        SDT_list.append(dartResult[i])
      else :
        bonus_list[num - 1] = dartResult[i]


    bonus_list = bonus_list[: num]

    for j in range(num) :

      SDT_list[j] = SDT_list[j].replace('S', '1')
      SDT_list[j] = SDT_list[j].replace('D', '2')
      SDT_list[j] = SDT_list[j].replace('T', '3')

  
    multi = 1
    answer = 0
    for i in range((num - 1), -1, -1) :
      if i == (num - 1) :
        if (bonus_list[i] == '*') :
          multi *= 2
          answer += int(num_list[i]) ** int(SDT_list[i]) * multi
        elif (bonus_list[i] == '#') :
          answer -= int(num_list[i]) ** int(SDT_list[i]) * multi
          multi = 1
        else :
          answer += int(num_list[i]) ** int(SDT_list[i]) * multi
          multi = 1
      
      elif (bonus_list[i] == '*') & (bonus_list[i + 1] == '*') :
        multi = 4
        answer += int(num_list[i]) ** int(SDT_list[i]) * multi
        multi = 2
      elif (bonus_list[i] == '*') & (bonus_list[i + 1] != '*') :
        multi = 2
        answer += int(num_list[i]) ** int(SDT_list[i]) * multi
      elif bonus_list[i] == '#' :
        answer -= int(num_list[i]) ** int(SDT_list[i]) * multi
        multi = 1
      else :
        answer += int(num_list[i]) ** int(SDT_list[i]) * multi
        multi = 1

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult) # 리스트 안의 튜플 꼴로 다 찾아준다.
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
# () : 그룹핑, 추출할 패턴을 지정한다.
# \d : 숫자를 의미
# + : 1회 이상 반복
# ? : 0회 이상 1회 이하




























def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)


