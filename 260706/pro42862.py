


def solution(n, lost, reserve):
    answer = 0

    possible_list = [False] * (n + 2)
    clothes_list = [False] * (n + 2)

    ## 수업 들을 수 있는 학생 리스트 
    for idx in range(n+2):
        if idx == 0 or idx == n +1:
            continue
        
        if idx in lost:
            continue

        possible_list[idx] = True

    ## 옷 빌려줄 수 있는 학생 리스트
    for idx in reserve:
        clothes_list[idx] = True


    for i in range(1, n+1, 1):
        if not possible_list[i] and clothes_list[i]:
            possible_list[i] = True
            clothes_list[i] = False

    for i in range(1, n+1, 1):
        front = i - 1
        back = i + 1
        if not possible_list[i]: ## 체육복이 없다면
            if clothes_list[front]:
                clothes_list[front] = False
                possible_list[i] = True
            elif clothes_list[back]:
                clothes_list[back] = False
                possible_list[i] = True

    
    for i in possible_list:  ## 체육복 있는 사람 다 세기
        if i:
            answer += 1

    
    return answer




n = 5
lost = [2, 4]
reserve = [1, 3, 5]

solution(n, lost, reserve)