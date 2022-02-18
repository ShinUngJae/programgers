# 내 코드

def solution(strings, n) :
    strings.sort()
    answer = sorted(strings, key = lambda x : x[n])
    return answer
