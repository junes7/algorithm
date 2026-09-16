from math import inf
from itertools import product
from copy import deepcopy
def solution(clockHands):
    rlt = inf
    length = len(clockHands)
    def rotation(board,x,y,n):
        deraction = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
        for dx,dy in deraction:
            nx = x + dx
            ny = y + dy
            if 0<= nx < length and 0<= ny < length:
                board[nx][ny] = (board[nx][ny] + n) % 4
    def finish(board):
        for x in board[-1]:
            if x != 0:
                return False
        return True
    for ns in product([0,1,2,3],repeat=length):
        cnt = 0 
        newboard = deepcopy(clockHands)
        for i,n in enumerate(ns):
            rotation(newboard,0,i,n) # 첫번째행 돌리기
            cnt += n
        
        for x in range(1,length):
            for y in range(length):
                if(r := newboard[x-1][y]) != 0:
                    rotation(newboard,x,y,(4-r)%4)
                    cnt += (4-r)%4   
        if finish(newboard):
            rlt = min(rlt,cnt)
    return rlt