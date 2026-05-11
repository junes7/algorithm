def solution(sequence, k):
    l = r = 0
    rlt = [0, len(sequence)]
    sum = sequence[0]
    while True:
        if sum < k:
            r += 1
            if r == len(sequence): break
            sum += sequence[r]
        else:
            if sum == k:
                if r-l < rlt[1]-rlt[0]:
                    rlt = [l, r]
            sum -= sequence[l]
            l += 1
    return rlt