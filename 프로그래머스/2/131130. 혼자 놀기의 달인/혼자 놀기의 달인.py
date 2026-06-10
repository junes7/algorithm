def solution(cards):
    rlt = []
    visited = [False] * (len(cards)+1) # 방문 체크
    for v in cards:
        if not visited[v]:
            tmp = []
            while v not in tmp:
                tmp.append(v)
                v = cards[v-1]
                visited[v] = True
            rlt.append(len(tmp))
    if rlt[0] == len(cards):
        return 0
    else:
        rlt.sort(reverse=True)
    return rlt[0] * rlt[1]