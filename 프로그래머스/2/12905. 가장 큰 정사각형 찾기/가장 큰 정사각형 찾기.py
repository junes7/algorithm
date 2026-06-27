def solution(board):
    n,m = len(board),len(board[0])  
    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    # 최대 넓이 구하기
    rlt = 0
    for i in range(n):
        temp = max(board[i])
        rlt = max(rlt, temp)
    return rlt**2