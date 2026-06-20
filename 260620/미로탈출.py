from collections import deque


def solution(maps):
    answer = 0
    map_x = len(maps)
    map_y = len(maps[0])

    visited = [[False] * map_y for _ in range(map_x)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]


    ## 시작 위치랑 레버 위치 찾기
    for i in range(map_x):
        for j in range(map_y):
            if maps[i][j] == "S":
                start_pos = (i, j)

            if maps[i][j] == "E":
                exit_pos = (i, j)
            
            if maps[i][j] == "L":
                lever_pos = (i, j)

            if maps[i][j] == "X":
                visited[i][j] = True
    
    base_visited = [row[:] for row in visited]


    def bfs(start_p, goal_p):
        nonlocal answer
        
        q = deque()
        q.append(start_p)
        dq = deque()
        visited[start_p[0]][start_p[1]] = True

        while q:
            dq = q
            q = deque()

            while dq:
                x, y = dq.popleft()

                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]

                    if 0 > nx or map_x <= nx or 0 > ny or map_y <= ny:
                        continue

                    if visited[nx][ny]:
                        continue 

                    q.append((nx, ny))
                    visited[nx][ny] = True
                    if (nx, ny) == goal_p:
                        answer += 1
                        return True

            answer += 1
            
        return False



    ## 시작 위치에서 레버위치까지 걸리는 시간 구하기
    if not bfs(start_pos, lever_pos):
        return -1

    ## 레버 위치에서 출구위치까지 걸리는 시간 구하기
    visited = base_visited
    if not bfs(lever_pos, exit_pos):
        return -1

    return answer