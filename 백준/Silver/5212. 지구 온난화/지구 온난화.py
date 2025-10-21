import sys
input=lambda:sys.stdin.readline().rstrip()
R, C = map(int, input().split())
current_map = ['.' * (C + 2)] + [('.' + input().strip() + '.') for _ in range(R)] + ['.' * (C + 2)]
pos_x = [1, -1, 0, 0]
pos_y = [0, 0, 1, -1]
point_set = set()
for i in range(1, R + 1):
    for j in range(1, C + 1):
        if current_map[i][j] == 'X':
            sea_num = 0
            for k in range(4):
                if current_map[i + pos_x[k]][j + pos_y[k]] == '.': sea_num += 1
            if sea_num < 3: point_set.add((i, j))
x_set = [p[0] for p in point_set]
y_set = [p[1] for p in point_set]
max_x, min_x, max_y, min_y = max(x_set), min(x_set), max(y_set), min(y_set)
for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        if (i, j) not in point_set: print('.', end='')
        else: print('X', end='')
    print()