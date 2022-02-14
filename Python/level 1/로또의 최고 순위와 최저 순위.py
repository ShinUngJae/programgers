# 내 코드
def solution(lottos, win_nums):
    zero = lottos.count(0)
    same = set(lottos) & set(win_nums)
    num = len(same)
    ans1 = 7 - (num + zero)
    ans2 = 7 - num
    if ans1 == 7 :
        ans1 = 6
    if ans2 == 7 :
        ans2 = 6
    answer = [ans1, ans2]
    return answer
  
  

  
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
