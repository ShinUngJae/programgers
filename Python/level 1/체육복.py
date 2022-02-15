# 내 코드
def solution(n, lost, reserve) :
    lost.sort()
    reserve.sort()

    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    stu = [i for i in range(1, n + 1)]
    for j in new_lost :
      if (j - 1) in new_reserve :
        new_reserve.remove(j - 1)
      elif (j + 1) in new_reserve :
        new_reserve.remove(j + 1)
      else :
        stu.remove(j)

    answer = len(stu)
    return answer
