



def solution(h1, m1, s1, h2, m2, s2):
    start_time = (h1 * 3600) + (m1 * 60) + s1
    end_time = (h2 * 3600) + (m2 * 60) + s2
    answer = 0

    def ceil_div(a, b):
        return (a + b - 1) // b

    def count_overlap(start, end, p, q):
        # 겹치는 시간: p * k / q
        # start <= p*k/q <= end
        # start*q <= p*k <= end*q

        left = ceil_div(start * q, p)
        right = (end * q) // p

        return max(0, right - left + 1)

    # 초침 - 분침
    answer += count_overlap(start_time, end_time, 3600, 59)

    # 초침 - 시침
    answer += count_overlap(start_time, end_time, 43200, 719)

    # 0시, 12시는 세 바늘이 모두 겹치므로 중복 1번 제거
    for t in [0, 43200]:
        if start_time <= t <= end_time:
            answer -= 1

    return answer