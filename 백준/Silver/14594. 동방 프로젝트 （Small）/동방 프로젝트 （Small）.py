import sys
input=lambda:sys.stdin.readline().rstrip()
N = int(input())
M = int(input())
rooms = [0] * (N+1)
for _ in range(M):
    x, y = map(int, input().split())
    for room in range(x, y):
        rooms[room] = 1
rlt = rooms.count(0)
print(rlt-1)