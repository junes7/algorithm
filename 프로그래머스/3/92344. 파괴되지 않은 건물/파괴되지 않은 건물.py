def solution(board, skill):
    n, m, cnt = len(board), len(board[0]), 0
    accumulate_sum = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    for attak_type, y1, x1, y2, x2, degree in skill:
        val = -degree if attak_type == 1 else degree
        accumulate_sum[y1][x1] += val
        accumulate_sum[y2 + 1][x2 + 1] += val
        accumulate_sum[y1][x2 + 1] -= val
        accumulate_sum[y2 + 1][x1] -= val
    for i in range(n + 1):
        for j in range(m):
            accumulate_sum[i][j + 1] += accumulate_sum[i][j]
    for j in range(m + 1):
        for i in range(n):
            accumulate_sum[i + 1][j] += accumulate_sum[i][j]
    return sum([1 for i in range(n) for j in range(m) if board[i][j] + accumulate_sum[i][j] > 0])