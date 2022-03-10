from itertools import permutations
import heapq as hq

def solution(numbers) :
    num_list = list(map(str, numbers))
    num_list.sort(key = lambda x : x * 3, reverse = True)
    answer = str(int(''.join(num_list)))

    return answer
    
# x * 3을 하는 이유
# num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하기 위해
# int로 변환한 뒤, 또 str로 변환해주는 이유
# 모든 값이 0일 때(즉, ‘000’을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환























































import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

# functools : 정렬 시 비교하는 함수를 만든다.
# 1, -1, 0이 설정되있는 함수를 만들어야 한다.
# 그 다음 cmp_to_key를 이용하여 지정해주면 된다.
  
  
  
  
  
  
