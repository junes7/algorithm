from collections import deque
n = int(input())  # 게임 구역의 크기 n 입력
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visit = []
# 방문 여부 체크 (초깃값 False로 설정)
for _ in range(n):
    visit.append([False]*n)
dx = [1, 0]
dy = [0, 1]
# 너비 우선 탐색(BFS) 알고리즘 함수 정의
def bfs(x, y, visit):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True
    while queue:
        x, y = queue.popleft()
        # 맨 오른쪽 아래에 도달하면 HaruHaru 출력
        if board[x][y] == -1:
            return 'HaruHaru'
        jump = board[x][y]
        # 오른쪽과 아래 탐색
        for i in range(2):
            # 좌표에 대한 이동은 기존 x, y 값에 점프값과 방향값을 곱하여 이동
            nx = x+dx[i]*jump
            ny = y+dy[i]*jump
            # 범위 안에 있고, 방문하지 않았으면 방문 체크 후 queue에 넣기
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = True
                queue.append((nx, ny))
    return 'Hing'
print(bfs(0, 0, visit))