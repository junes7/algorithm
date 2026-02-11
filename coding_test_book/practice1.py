import sys
input=lambda:sys.stdin.readline().rstrip()
d = {'.': 46, 'O': 79, '-': 124, '|': 45, '/': 92, '\\': 47,
     '^': 60, '<': 118, 'v': 62, '>': 94}
N, M = map(int, input().split())
box = []
for _ in range(N):
    box.append(input())
rotate = []  # 왼쪽으로 돌린 후 결과
for i in range(M - 1, -1, -1):
    row = []  # 돌린 후 i 행의 결과
    for j in range(N):
        row.append('%c' % d[box[j][i]])
    rotate.append(row)
for r in rotate:
    print(''.join(r))