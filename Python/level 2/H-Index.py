def solution(citations):
    citations = sorted(citations)
    c = len(citations)
    for i in range(c):
        if citations[i] >= c-i:
            return c-i
    return 0
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
