import heapq
def solution(operations):
    rlt = []
    q = []
    for operation in operations:
        x, num = operation.split() 
        num = int(num)
        if x == 'I':
            heapq.heappush(q, num)
        elif x == 'D' and num == 1:
            if len(q) != 0:
                max_value = max(q)
                q.remove(max_value)
        else:
            if len(q) != 0:
                heapq.heappop(q)
    if len(q) == 0:
        rlt = [0, 0]
    else:
        rlt = [max(q), heapq.heappop(q)]    
    return rlt