import sys
input=lambda:sys.stdin.readline().rstrip()
from collections import deque
r, c = map(int, sys.stdin.readline().split())
grass = []
for _ in range(r):
    grass.append(list(sys.stdin.readline().rstrip()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    grass[x][y] = "."
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= r or ny >= c or nx < 0 or ny < 0:	#배열범위를 벗어난 경우 건너뛰기
                continue
            if grass[nx][ny] == ".":	#값이 .인 경우 건너뛰기
                continue
            if grass[nx][ny] == "#":	#값이 #인 경우
                grass[nx][ny] = "."	#방문했으니 다른 값으로 덮어씌우기
                queue.append((nx, ny))	#nx, ny를 기준으로 순회할 수 있도록 nx, ny를 queue에 넣어준다.
answer = 0
for i in range(r):
    for j in range(c):
        if grass[i][j] == "#":
            bfs(i, j)
            answer += 1
print(answer)