def solution(info, edges):
    rlt = []
    visited = [False] * len(info)
    def dfs(sheeps, wolves):
        # 현재까지 모은 양이 늑대보다 많으면 경로 유지, 그렇지 않으면 탐색 중단
        if sheeps > wolves:
            rlt.append(sheeps)
        else:
            return
        # 모든 간선을 순회하며 이동 가능한 경로 탐색
        for p, c in edges:
            # 부모 노드 p는 방문했으나, 자식 노드 c는 아직 방문하지 않은 경우에만 진행
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:  # 양인 경우
                    dfs(sheeps + 1, wolves)
                else:           # 늑대인 경우
                    dfs(sheeps, wolves + 1)
                # 다른 경로 탐색을 위해 방문 상태 초기화
                visited[c] = False
    # 루트 노드(0번)는 시작점이므로 방문 처리
    visited[0] = True
    dfs(1, 0)
    return max(rlt)