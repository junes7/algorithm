def solution(dist_limit, split_limit):
    rlt = 1
    def dfs(product,leaves, available, used):
        nonlocal rlt
        # 현재 리프 개수 갱신
        rlt = max(rlt, leaves)
        # 분배 노드 더 못 쓰면 종료
        if used == dist_limit:
            return
        # 다음 깊이를 2분기 또는 3분기로 선택
        for branch in [2,3]:
            # 분배도 제한 초과
            if product * branch > split_limit:
                continue
            # 실제 확장 가능한 노드 수
            expand = min(available, dist_limit - used)  
            # 새 리프 개수
            new_leaves = leaves + expand * (branch - 1)
            # 사용한 분배 노드 수
            new_used = used + expand
            # 다음 깊이에서 확장 가능한 노드 수
            new_available = expand * branch
            dfs(
                product * branch,
                new_leaves,
                new_available,
                new_used
            )      
    # 시작 상태
    dfs(1,1,1,0)
    return rlt