def solution(s) :
  
    number1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i, j in zip(number1, number2) :
      s = s.replace(i, j)

    answer = int(s)
    return answer
  
  
  
  


num_dic = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

def solution(s):
    answer = s
    for key, value in num_dic.items() :
        answer = answer.replace(key, value)
    return int(answer)
  
  
  
  
  
  
  
  
  
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)) :
        s = s.replace(words[i], str(i))

    return int(s)
