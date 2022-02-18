# 내 코드
def solution(s) :
    answer = ((len(s) == 4) or (len(s) == 6)) and (s.isdigit())
    return answer
  
  
  
  
  
  
  
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
  
  
  
  
  
  
import re
def alpha_string46(s):
    return bool(re.match("^(\d{4}|\d{6})$", s))
