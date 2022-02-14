def solution(numbers, hand) :
  
  pad = {}

  for i in range(0, 10) :
    if i == 0 :
      pad[i] = [4, 2]
    elif i in range(1, 4) :
      pad[i] = [1, i]
    elif i in range(4, 7) :
      pad[i] = [2, i - 3]
    else :
      pad[i] = [3, i - 6]

  left_num = [4, 1]
  right_num = [4, 3]
  answer = ''

  for i in numbers :
    if pad[i][1] == 1 :
      answer += 'L'
      left_num = pad[i]
    elif pad[i][1] == 3 :
      answer += 'R'
      right_num = pad[i]
    elif pad[i][1] == 2 :
      left_dist = abs(left_num[0] - pad[i][0]) + abs(left_num[1] - pad[i][1])
      right_dist = abs(right_num[0] - pad[i][0]) + abs(right_num[1] - pad[i][1])
      if left_dist > right_dist :
        answer += 'R'
        right_num = pad[i]
      elif left_dist < right_dist :
        answer += 'L'
        left_num = pad[i]
      elif hand == 'left' :
        answer += 'L'
        left_num = pad[i]
      else :
        answer += 'R'
        right_num = pad[i]

  return answer
