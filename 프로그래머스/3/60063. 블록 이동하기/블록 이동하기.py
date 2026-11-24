from collections import deque
def get_next_pos(pos, bd):
    npos = []
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상하좌우 이동
    dx,dy = [0, 1, 0, -1],[-1, 0, 1, 0]
    for i in range(4):
        nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
        if bd[nx1][ny1] == 0 and bd[nx2][ny2] == 0:
            npos.append({(nx1, ny1), (nx2, ny2)})
    # 회전 이동
    turn = [-1, 1]
    # 로봇이 가로로 놓여 있는 경우
    if x1 == x2:
        for t in turn:
            if bd[x1+t][y1] == 0 and bd[x2+t][y2] == 0:
                npos.append({(x1, y1), (x1+t, y1)})
                npos.append({(x2, y2), (x2+t, y2)})
    elif y1 == y2:
        for t in turn:
            if bd[x1][y1+t] == 0 and bd[x2][y2+t] == 0:
                npos.append({(x1, y1), (x1, y1+t)})
                npos.append({(x2, y2), (x2, y2+t)})
    return npos
def solution(bd):
    n = len(bd)
    newbd = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            newbd[i+1][j+1] = bd[i][j]
    queue = deque()
    pos = {(1, 1), (1, 2)}
    queue.append((pos, 0))
    visited = []
    visited.append(pos)
    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, newbd):
            if next_pos not in visited:
                queue.append((next_pos, cost+1))
                visited.append(next_pos)
    return cost