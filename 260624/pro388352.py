



def solution(n, q, ans):
    answer = 0
    

    ## 정답 체크 로직/ 아니 이걸 이렇게 일일히 하는게 맞나
    def check_ans(secret_code):
        for i in range(len(q)):
            cnt = 0

            for num in q[i]:
                if num in secret_code:
                    cnt += 1
            
            if cnt != ans[i]:
                return False
        
        return True


    def dfs(secret_code, idx):
        nonlocal answer

        ## 리스트 꽉차면 정답 체크
        if len(secret_code) == 5:
            if check_ans(secret_code):
                answer += 1
            return


        ## 재귀 돌리기/ 오름차순이니깐 1씩 큰값부터 돌리기
        for i in range(idx+1, n+1, 1):
            secret_code.append(i)
            dfs(secret_code, i)
            secret_code.pop()



    dfs([], 0)  ## 비밀코드, 자리


    return answer