def solution(targets):
    targets.sort(key = lambda x:[x[1],x[0]])
    rlt,s,e = 0,0,0
    for x in targets:
        if(x[0]>=e):
            e = x[1]
            rlt += 1
    return rlt