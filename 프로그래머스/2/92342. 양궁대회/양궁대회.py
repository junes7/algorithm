from itertools import combinations_with_replacement
from collections import Counter
def solution(n, info):
    rlt = []
    maxN = -1
    info = info[::-1]
    lenI = len(info)
    # 맞힌 개수에 대해 전체 조합을 구함
    for c in combinations_with_replacement(range(11),n):
        ryan = 0
        apeach = 0
        tmpRlt = [0 for _ in range(lenI)]
        c = Counter(c) # 특정 조합에 대해 Counter을 구함
        # 특정 조합의 맞힌 개수 비교해서 점수 저장
        for i in range(lenI) :
            if info[i] < c[i] :
                ryan += i
            elif info[i] != 0 :
                apeach += i
            tmpRlt[i] = c[i]   
        # 라이언의 점수가 더 높을 경우
        if ryan > apeach :
            diff = ryan - apeach # 점수차를 구함
            if maxN < diff :
                maxN = diff
                rlt = tmpRlt
    if rlt :
        return rlt[::-1]
    else :
        return [-1]