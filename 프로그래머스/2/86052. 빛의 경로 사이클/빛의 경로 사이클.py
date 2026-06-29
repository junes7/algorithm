def solution(grid):
    rlt = []
    r, c = len(grid), len(grid[0])
    board = [[[] for _ in range(c)] for _ in range(r)]
    directions = {'U':[1,0], 'R':[0,1], 'D':[-1,0], 'L':[0,-1]}
    for x in range(r):
        for y in range(c):
            for d in 'ULDR':
                move = 0
                while True:
                    if d in board[x][y]: break
                    board[x][y].append(d)
                    move += 1
                    x = (x + directions[d][0]) % r
                    y = (y + directions[d][1]) % c
                    if grid[x][y] == 'L':
                        idx = 'ULDR'.index(d)
                        d = 'ULDR'[0] if idx == 3 else 'ULDR'[idx+1]
                    elif grid[x][y] == 'R':
                        idx = 'URDL'.index(d)
                        d = 'URDL'[0] if idx == 3 else 'URDL'[idx+1]             
                if move > 0 : rlt.append(move)
    return sorted(rlt)