def pop_set(m, n, board):
    pop_set = set()
    for r in range(1, n):
        for c in range(1, m):
            if board[r][c] == board[r-1][c-1] == board[r-1][c] == board[r][c-1] != '_':
                # pop_set.update(set([(r, c), (r-1, c-1), (r-1, c), (r, c-1)]))
                pop_set |= set([(r, c), (r-1, c-1), (r-1, c), (r, c-1)])

    for r, c in pop_set:
        board[r][c] = 0
    for idx, row in enumerate(board):
        empty = ['_'] * row.count(0)
        board[idx] = empty + [block for block in row if block != 0]
    return len(pop_set)

def solution(m, n, board):
    board = list(map(list, zip(*board)))
    rlt = 0
    while True:
        cnt = pop_set(m, n, board)
        if cnt == 0: return rlt
        rlt += cnt