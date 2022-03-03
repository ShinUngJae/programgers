def goto(grid, visited, start):
    x, y, way = start
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    length = 0
    while True:
        if visited[x][y][way]:
            break
 
        visited[x][y][way] = True # 방문한 곳은 True로 변환
        length += 1 # 사이클 길이
 
        if grid[x][y] == 'S':
            pass
        elif grid[x][y] == 'L':
            way = (way + 1) % 4 # 방향 전환
        elif grid[x][y] == 'R':
            way = (way - 1) % 4 # 방향 전환
 
        x = (x + direction[way][0]) % len(grid) # 가로 길이를 넘어갔을 때, 반대편 가로로
        y = (y + direction[way][1]) % len(grid[0]) # 세로 길이를 넘어갔을 때, 반대편 세로로
 
    return length
 
def solution(grid):
    answer = []
    visited = [[[False] * 4 for _ in range(len(grid[0]))] for __ in range(len(grid))]
 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                if visited[i][j][k] == False: 
                    answer.append(goto(grid, visited, [i, j, k]))

    # 일반적으로 한번 방문한 방향이 True면 그 사이클은 이미 한번 돌았던 사이클임
    # 반대로 False라면 새로운 사이클인 것
 
    answer.sort()
    return answer
