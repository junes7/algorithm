from collections import deque
def solution(S, K):
    rlt = 0 
    mix = deque()
    S.sort()
    sco = deque(i for i in S)
    while (sco and sco[0] < K) or (mix and mix[0] < K):
        rlt += 1
        if len(sco) + len(mix) <= 1:
            return -1      
        food = [0]*2
        for a in range(2):
            if sco and mix:
                if sco[0] < mix[0]:
                    food[a] = sco.popleft()
                else:
                    food[a] = mix.popleft()
            elif sco:
                food[a] = sco.popleft()
            else:
                food[a] = mix.popleft()       
        mix.append(food[0]+food[1]*2)  
    return rlt