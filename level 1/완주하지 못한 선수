import collections

def solution(participant, completion) :
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    



def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()
    
    
    
    
def solution(participant, completion) :
    
    temp = 0
    dic = {}
    
    for i in participant :
        dic[hash(i)] = i
        temp += int(hash(i))
    for j in completion :
        temp -= hash(j)
        answer = dic[temp]
    
    return answer    
