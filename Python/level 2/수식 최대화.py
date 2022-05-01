# 내 코드
import re
from itertools import permutations

def solution(expression) :
    number = re.findall('[0-9]+', expression)
    calculation = re.findall('[-*+]', expression)
    seq = list(permutations(set(calculation), len(set(calculation))))

    answers = []
    number_list = number
    calculation_list = calculation
    for s in seq :
      number_list = number.copy()
      calculation_list = calculation.copy()
      for i in range(len(set(calculation))) :
        while calculation_list.count(s[i]) > 0 :
          cal_index = calculation_list.index(s[i])
          formula = number_list[cal_index] + s[i] + number_list[cal_index + 1]
          number_list[cal_index] = str(eval(formula))
          number_list.pop(cal_index + 1)
          calculation_list.pop(cal_index)
      answers.append(abs(int(number_list[0])))
      
    answer = max(answers)

    return answer
  
  
# 순열 -> from itertools import permutations
# 조합 -> from itertools import combinations
# 중복순열 -> from itertools import products # repeat
# 중복조합 -> from itertools import combinations_with_replacement # repeat


