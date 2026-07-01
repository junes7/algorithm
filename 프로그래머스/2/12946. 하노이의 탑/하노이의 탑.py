def hanoi(start, end, extra, n, rlt):
        if n == 1:
            rlt.append([start, end])
        else:
            hanoi(start, extra, end, n-1, rlt)
            hanoi(start, end, extra, 1, rlt)
            hanoi(extra, end, start, n-1, rlt)
        return rlt   
def solution(n):
    rlt = hanoi(1, 3, 2, n, [])
    return rlt