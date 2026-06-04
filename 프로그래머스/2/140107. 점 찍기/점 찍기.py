def solution(k, d):
    rlt = 0 
    for x in range(0,d+1,k) :
        max_y = int( (d**2 - x**2)**0.5 )
        rlt += (max_y // k) +1 
    return rlt