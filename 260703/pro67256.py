

def solution(numbers, hand):
    answer = ''

    ## 좌표 계산용으로 dict으로 관리
    number_pad = {
        1 : (0, 0),
        2 : (0, 1),
        3 : (0, 2),
        4 : (1, 0),
        5 : (1, 1),
        6 : (1, 2),
        7 : (2, 0),
        8 : (2, 1),
        9 : (2, 2),
        0 : (3, 1),
        "#" : (3, 2),
        "*" : (3, 0),
    }

    left_hand = number_pad["*"]
    right_hand = number_pad["#"]
    left_num = [1, 4, 7]
    right_num = [3, 6, 9]


    for n in numbers:

        if n in left_num:  ## 왼쪽번호면 왼손 추가
            answer += "L"
            left_hand = number_pad[n]
            continue

        if n in right_num:  ## 오른쪽번호면 오른손 추가
            right_hand = number_pad[n]
            answer += "R"
            continue

        ## 거리 비교
        left = abs(left_hand[0] - number_pad[n][0]) + abs(left_hand[1] - number_pad[n][1])
        right = abs(right_hand[0] - number_pad[n][0]) + abs(right_hand[1] - number_pad[n][1])

        if left > right:
            answer += "R"
            right_hand = number_pad[n]
        elif right > left:
            answer += "L"
            left_hand = number_pad[n]
        else:
            if hand == "right":
                answer += "R"
                right_hand = number_pad[n]
            if hand == "left":
                answer += "L"
                left_hand = number_pad[n]

    return answer