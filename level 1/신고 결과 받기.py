def solution(id_list, report, k) :
    
    answer = [0] * len(id_list)
    reported_dict = {x : [] for x in id_list}
    for i in set(report) :
        a = i.split()[1]
        b = i.split()[0]
        reported_dict[a].append(b)
    
    for key, value in reported_dict.items() :
        if len(value) >= k :
            for j in value :
                answer[id_list.index(j)] += 1

    return answer
