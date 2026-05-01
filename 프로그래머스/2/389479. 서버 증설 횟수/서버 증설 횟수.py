def solution(players, m, k):
    server = [0 for _ in range(len(players))]
    server_cnt = 0
    for i in range(len(players)):
        n = 0
        if players[i] >= m:
            n = players[i] // m
            # 기존 서버로 할당 가능한지 확인
            add_server_cnt = 1
            if server[i] < n:
                # 기존 서버로 할당 불가능하다면, 불가능한 수 만큼 증설
                add_server_cnt = n - server[i] # 증설해야할 서버 수
                if n * m <= players[i] < (n+1) * m:
                    server_cnt += add_server_cnt
                    for j in range(k):
                        if i + j < len(server):
                            server[i+j] += add_server_cnt       
                        else:
                            break
    return server_cnt