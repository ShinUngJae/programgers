# 좌우와 상하를 따로 구해서 더하자!

def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx) # 왼쪽이 더 빠른지 오른쪽이 더 빠른지 결정
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer
    
    
# 이 문제는 상당히 더럽다
