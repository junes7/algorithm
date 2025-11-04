import sys
input=lambda:sys.stdin.readline().rstrip()
d = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1)]
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    board = [list(input().rstrip()) for _ in range(n)]
    # 판을 순회하며 주변의 지뢰 수 탐색
    for x in range(n):
        for y in range(m):
            # 지뢰는 변경 x
            if board[x][y] == '*':
                continue
            cnt = 0
            for a, b in d:
                dx, dy = x+a, y+b
                # 인덱스 벗어나는 경우 
                if dx >= n or dx < 0 or dy >= m or dy < 0:
                    continue
                if board[dx][dy] == '*':
                    cnt += 1
            board[x][y] = str(cnt)
    for row in board:
        print(''.join(row))