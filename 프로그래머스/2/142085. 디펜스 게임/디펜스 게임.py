from heapq import heappop, heappush
def solution(n, k, enemy):
    rlt, sumE = 0, 0
    heap = []
    for e in enemy:
        heappush(heap, -e)
        sumE += e
        if sumE > n:
            if k == 0: break
            sumE += heappop(heap) 
            k -= 1
        rlt += 1
    return rlt