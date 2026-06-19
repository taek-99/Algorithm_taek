## 21분 소요

def solution(board, h, w):
    answer = 0

    board_x = len(board)
    board_y = len(board[0])

    dx = [0, 1, -1, 0]
    dy = [-1, 0, 0, 1]

    for idx in range(4):
        nx = h + dx[idx]
        ny = w + dy[idx]

        ## 범위 벗어나면 스킵
        if nx < 0 or nx >= board_x or ny < 0 or ny >= board_y:
            continue

        ## 색 같은지 확인
        if board[h][w] == board[nx][ny]:
            answer += 1

    return answer