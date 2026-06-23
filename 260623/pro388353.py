from pprint import pprint
from collections import deque


def solution(storage, requests):
    answer = 0
    n = len(storage)
    m = len(storage[0])

    visited = [[False] * m for _ in range(n)]
    out_storage = [[False] * m for _ in range(n)]

    ## 외곽 컨테이너 구별
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1:
                out_storage[i][j] = True

            if j == 0 or j == m-1:
                out_storage[i][j] = True


    def out_check():
        nonlocal out_storage

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()

        for x in range(n):
            for y in range(m):
                if visited[x][y] and out_storage[x][y]:
                    q.append((x, y))


                    while q:
                        mx, my = q.popleft()
                        
                        for idx in range(4):
                            nx = mx + dx[idx]
                            ny = my + dy[idx]

                            if 0 > nx or n <= nx or 0 > ny or m <= ny: ## 범위 벗어나면 스킵
                                continue

                            if out_storage[nx][ny]:
                                continue
                            
                            out_storage[nx][ny] = True
                            
                            if visited[nx][ny]:
                                q.append((nx, ny))



    for request in requests: 
        # print ("===========")
        # pprint(visited)
        out_check()
        for i in range(n):
            for j in range(m):

                if len(request) == 1:
                    if out_storage[i][j]: ## 외곽만 해야될때
                        if storage[i][j] == request[0]: ## 같은 알파벳 처리
                            visited[i][j] = True

                else:  ## 크레인으로 뽑아낼때
                    if storage[i][j] == request[0]: ## 같은 알파벳 처리
                        visited[i][j] = True


    for i in range(n):  ## 남은 컨테이너 갯수 세기
        for j in range(m):
            if not visited[i][j]:
                answer += 1


    return answer




# storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
# requests = ["A", "BB", "A"]

# solution(storage, requests)