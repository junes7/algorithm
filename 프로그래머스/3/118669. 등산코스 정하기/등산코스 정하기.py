from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    MAX = 10000001
    rlt = [0, MAX]
    # 0. summits을 list -> set으로 변경 : O(n)
    set_summits = set(summits)
    # 1. paths를 graph로 변경 (양방향)
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    # 2. dijkstra algorithm
    min_dis = [MAX for _ in range(n+1)] # ! (n+1) 주의
    # 2.1 우선순위 큐에 시작노드 gates 한 번에 넣기
    pq = [(0, gate) for gate in gates]
    while pq:
        # 2.2 우선순위 가장 높은 노드 추출
        intensity, cur_v = heapq.heappop(pq)
        '''
        # 2.3 방문여부 확인
        # if cur_v not in costs:
        #     costs[cur_v] = intensity
        '''
        # 2.3 방문여부 확인 대신에 min_dis[cur_v]보다 intensity가 더 작은값이면 갱신
        if min_dis[cur_v] > intensity:
            # 2.4 비용 업데이트
            min_dis[cur_v] = intensity
        else: # 크거나 같으면 무시
            continue
        # 2.5 현재 노드와 연결된 노드 우선순위 큐에 추가
        for cost, next_v in graph[cur_v]:
            # 현재 cost와 다음 cost 비교해서 next_cost 구하기
            next_cost = max(intensity, cost)
            if min_dis[next_v] <= next_cost:
                continue
            # heappush 전에 산봉우리 노드 만나면 continue
            if cur_v in set_summits: # 탐색시 시간복잡도 줄이기 list=O(n) -> set=O(1)
                continue
            heapq.heappush(pq, (next_cost, next_v))
    # 3. summits 돌면서 rlt 구하기
    for summit in summits:
        # min_dis(summit)이 최저 intensity보다 작으면
        if rlt[1] > min_dis[summit]:
            rlt = [summit, min_dis[summit]]
        # intensity가 같으면 산봉우리 번호가 작은 값 선택
        elif rlt[1] == min_dis[summit] and summit < rlt[0]:
            rlt[0] = summit
    return rlt