def solution(A, B):
    rlt = 0
    A.sort()
    B.sort()
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            rlt += 1
            i += 1
        j += 1
    return rlt