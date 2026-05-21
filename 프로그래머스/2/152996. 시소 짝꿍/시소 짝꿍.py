from collections import Counter
def solution(weights):
    rlt = 0
    # 1:1
    counter = Counter(weights)
    for k,v in counter.items():
        if v>=2:
            rlt+= v*(v-1)//2
    weights = set(weights)
    # 2:3 2:4 3:4 비율 가지면 짝궁 가능함
    for w in weights:
        if w*2/3 in weights:
            rlt+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            rlt+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            rlt+= counter[w*3/4] * counter[w]
    return rlt