

def solution(players, m, k):
    answer = 0
    servers = []  ## 서버
    server_capacity = m ## 서버 가용 인원


    for player in players:    
        server_cnt = len(servers) ## 사용중인 서버 개수

        if player > server_capacity * server_cnt: ## 현재 사용자수가 서버 가용상태를 넘을 경우 증설
            need_servers = (player // server_capacity) - server_cnt  ## 필요한 서버 수
            
            for _ in range(need_servers): ## 서버 추가
                servers.append(k)
                answer += 1
        
        servers = [idx - 1 for idx in servers if idx - 1 > 0] ## 증설된 서버 시간 감소

    
    return answer