def solution(begin, end):
    rlt = []
    for n in range(begin,end+1):
        rlt.append(maxBlock(n))
    return rlt
def maxBlock(n):
    tmp = [1]
    if(n == 1) :
        return 0
    for i in range(2,int(n**(1/2))+1):
        if(n%i == 0 and i <= 10**7) :
            tmp.append(i)
            if(n//i <=10**7 and n//i != n):
                tmp.append(n//i)
    return max(tmp)