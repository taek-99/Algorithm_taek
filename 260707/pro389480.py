



def solution(info, n, m):
    num = len(info)
    INF = 10**9
    memo = {}

    def dfs(idx, a_doduk, b_doduk):

        if idx == num:  ## 완료
            return a_doduk
        
        if a_doduk >= n or b_doduk >= m:  ## 가지치기
            return INF
        
        key = (idx, a_doduk, b_doduk)
        if key in memo:
            return memo[key]

        a_thing, b_thing = info[idx]
        result = INF

        # A가 훔치는 경우
        next_a = a_doduk + a_thing
        if next_a < n:
            aa = dfs(idx + 1, next_a, b_doduk)
            result = min(result, aa)

        # B가 훔치는 경우
        next_b = b_doduk + b_thing
        if next_b < m:
            bb = dfs(idx + 1, a_doduk, next_b)
            result = min(result, bb)

        memo[key] = result
        return result

    answer = dfs(0, 0, 0)

    if answer == INF:
        return -1

    return answer