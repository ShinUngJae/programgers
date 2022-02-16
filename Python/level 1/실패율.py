def solution(N, stages) :
    prob = [0 for _ in range(N)]
    stages.sort()

    for i in set(stages) :
      if i > N :
        pass
      else :
        prob[i - 1] = stages.count(i) / len(stages)
        stages = [j for j in stages if j != i]

    answer = sorted(range(1, N + 1), key = lambda k : prob[k - 1], reverse = True)
    return answer
