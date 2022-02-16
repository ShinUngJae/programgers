# 내 코드
def solution(nums) :
    
    pocket_nums = int(len(nums) / 2)
    pocket_species = len(set(nums))
    answer = pocket_nums

    if pocket_nums > pocket_species :
      answer = pocket_species
    return answer
  
  
  
  
  
  
  
  
  
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
