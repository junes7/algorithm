import sys, heapq
def solution(n, s, a, b, fares):
    INF = sys.maxsize
    # 문제에서 주어진 fares를 인접리스트 형태로 바꿈
    maps = [[] for _ in range(n+1)]
    for v,u,c in fares:
        maps[v].append((u, c))
        maps[u].append((v, c))
    # 다익스트라 알고리즘으로 구현
    def dijkstra(start):
        dist = [INF] * (n+1)
        dist[start] = 0
        que = [(0, start)]
        while que:
            cur_dist, cur_node = heapq.heappop(que)
            if dist[cur_node] < cur_dist:
                continue
            for next_node, next_dist in maps[cur_node]:
                if dist[next_node] > cur_dist + next_dist:
                    dist[next_node] = cur_dist + next_dist
                    heapq.heappush(que, (cur_dist + next_dist, next_node))
        return dist
    # i번째(특정 노드)에서 시작해서 모든 정점으로 도착하는 최단거리를 미리 구함 
    D = [0] + [dijkstra(i) for i in range(1, n+1)] 
    path = INF
    for i in range(1, n+1):
        path = min(path, D[s][i] + D[i][a] + D[i][b])
    return path