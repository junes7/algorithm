from collections import *
dx,dy=[-1,1,0,0],[0,0,1,-1]
def solution(board):
    N,M,q = len(board),len(board[0]),deque()
    dist = [[987654321 for _ in range(M)] for _ in range(N)]
    # 로봇(R)의 시작 위치를 찾아 큐에 추가
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i,j,0))
                dist[i][j] = 0
        if q:
            break
    while q:
        x,y,c = q.popleft()
        # 목표 지점(G)에 도착한 경우 이동 횟수 반환
        if board[x][y] == 'G':
            return c
        # 네 방향으로 이동할 수 있는 경우 탐색
        for i in range(4):
            n_x,n_y = x,y
            # 해당 방향으로 미끄러지며 이동 가능한 위치 찾기
            while 0<=n_x+dx[i]<N and 0<=n_y+dy[i]<M and board[n_x+dx[i]][n_y+dy[i]] != 'D':
                n_x += dx[i]
                n_y += dy[i]
            # 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if dist[n_x][n_y] > c+1:
                dist[n_x][n_y] = c+1
                q.append((n_x,n_y,c+1))
    # 목표 지점에 도착할 수 없는 경우 -1 반환
    return -1