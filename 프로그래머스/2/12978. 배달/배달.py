import heapq
def solution(N, road, K):
    rlt = 0
    graph = [[] for _ in range(N + 1)]
    for info in road:
        st = info[0]
        end = info[1]
        time = info[2]
        graph[st].append([end, time])
        graph[end].append([st, time])
    def dijkstra(graph, st):
        times = [float('inf') for _ in range(N + 1)]
        times[st] = 0
        queue = []
        heapq.heappush(queue, [times[st], st])
        while (queue):
            current_time, current_end = heapq.heappop(queue)
            if (times[current_end] < current_time):
                continue
            for new_end, new_time in graph[current_end]:
                time = current_time + new_time
                if (time < times[new_end]):
                    times[new_end] = time
                    heapq.heappush(queue, [time, new_end])
        return times
    result = dijkstra(graph, 1)
    for i in result:
        if (i <= K):
            rlt += 1
    return rlt