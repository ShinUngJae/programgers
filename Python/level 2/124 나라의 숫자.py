def solution(n) :
    answer = ''
    OTF_num = ['1', '2', '4']
    while n > 0 :
      n -= 1
      answer = OTF_num[(n % 3)] + answer
      n = n // 3

    return answer
  
  
  
  
  
  
  
  
  
  
  
  
  
 
  
  
  
def change124(n) :
    if n <= 3 :
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
  def change124(n):
    answer = "0"

    return ['4', '1', '2'][n%3] if n < 4 else change124((n-1) // 3) + ['4', '1', '2'][n%3]
