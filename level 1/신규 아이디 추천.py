import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st) 
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
    

# re.sub(a, b, c) c에서 a인 문자를 b로 바꾸자. (R의 gsub과 같은 함수)
# [^~~~~~~~] : 을 제외한 문자
# ^ : 문자열의 처음
# $ : 문자열의 끝
# . : 모든 문자    
# * : 앞에 있는 문자가 0부터 무한대로 반복    
# + : 앞에 있는 문자가 1부터 무한대로 반복    
# {m, n} : 앞에 있는 문자의 반복 횟수가 m번 부터 n번 까지 반복    
# ? : 앞에 있는 문자의 반복 횟수가 0번 부터 1번 까지 반복    
# . ^ $ * + ? { } [ ] \ | ( )의 문자 그대로를 나타내고 싶으면 앞에 \을 붙여야 함    
    
    
    
    
    
    
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3 -> 눈 여겨봐야 할 곳
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
    
    
    
    
# 내 코드
def solution(new_id) :
    phase_1 = new_id.lower()
    
    phase_2 = ''
    for i in phase_1 :
        if (i.islower()) or (i.isdigit()) or (i == '-') or (i == '_') or (i == '.') :  
            phase_2 += i
    
    phase_3 = ''
    for j in range(len(phase_2)) :
        if j == 0 :
            phase_3 += phase_2[j]
            end = phase_2[j]
        elif (end == '.') & (phase_2[j] == '.') :
            end = phase_2[j]
        else :
            phase_3 += phase_2[j] 
            end = phase_3[-1]
            
    phase_4 = phase_3.strip('.')
    
    if len(phase_4) == 0 :
        phase_4 = 'a'
    phase_5 = phase_4
    
    if len(phase_5) > 15 :
        phase_5 = phase_5[: 15]
    phase_6 = phase_5.strip('.')
    
    if len(phase_6) < 3 :
        temp = phase_6[-1]
        phase_6 = phase_6 + temp * (3 - len(phase_6))
    phase_7 = phase_6
    
    answer = phase_7

    return answer
