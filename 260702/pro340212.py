def solution(diffs, times, limit):
    answer = 0
    n = len(diffs)

    def check(level):
        tt = 0
        for idx in range(n):
            ## 레벨이 난이도보다 높으면 시간 바로 추가
            if diffs[idx] <= level:
                tt += times[idx]
            else:
                ## 레벨이 난이도보다 낮을 경우 이전 퍼즐 시간과 현재 퍼즐시간을 더한후
                ## 레벨과 난이도 차이만큼 더해줌
                k = diffs[idx] - level
                t = ((times[idx] + times[idx-1]) * k) + times[idx]
                tt += t
            if tt > limit:
                return False

        return True

    left = 1
    right = max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer