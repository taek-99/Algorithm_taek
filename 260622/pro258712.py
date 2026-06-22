



def solution(friends, gifts):
    answer = 0

    n = len(friends)
    board = [[0] * n for _ in range(n)]
    name_match = {val: idx for idx, val in enumerate(friends)}
    gift_index = [0] * n
    next_month_get_gift = [0] * n

    ## 선물 주고 받은 거 정리
    for gift in gifts:
        user, target = gift.split()  ## 띄어쓰기를 기준으로 주는사람, 받는사람 구분
        board[name_match[user]][name_match[target]] += 1

    ## 선물 지수 정리
    for idx in range(n):
        put_gift = sum(board[idx])
        get_gift = sum(row[idx] for row in board)
        gift_index[idx] = put_gift - get_gift

    ## 서로 비교
    for i in range(n):
        for j in range(n):

            if i == j: ## 같은 사람은 스킵
                continue

            if board[i][j] > board[j][i]:  ## 상대보다 선물 더 많이 줬으면 +1
                next_month_get_gift[i] += 1
                continue

            if board[i][j] == board[j][i]:  ## 주고받은 갯수가 같으면 선물 지수로 비교
                if gift_index[i] > gift_index[j]:  # 선물지수가 높으면 +1
                    next_month_get_gift[i] += 1

    answer = max(next_month_get_gift)
    return answer