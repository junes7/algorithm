def solution(n):
    rlt = dfsQueen([0]*n,0,n)
    return rlt
def dfsQueen(board,row,n):
    cnt = 0
    if n == row:
        return 1
    for col in range(n) :
        board[row] = col
        for i in range(row):
            if board[i] == board[row]:
                break
            if abs(board[i]-board[row]) == row - i:
                break
        else :
            cnt += dfsQueen(board,row+1,n)
    return cnt