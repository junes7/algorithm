def solution(n, stations, w):
    rlt = 0
    std = w * 2 + 1
    st = 1
    for s in stations:
        if s - w - st > 0:
            rlt += (s - w - st)//std
            if (s - w - st)%std: rlt += 1
        st = s + w + 1
    if n - st + 1 > 0:
        rlt += (n - st + 1) // std
        if (n - st + 1)%std: rlt += 1
    return rlt