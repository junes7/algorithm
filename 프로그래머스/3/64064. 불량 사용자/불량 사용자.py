import re
from itertools import permutations
def solution(user_id, banned_id):
    rlt=0
    # 모든 조합 구하기
    rlts = []
    for p in permutations(user_id, len(banned_id)):
        cnt = 0
        for i in range(len(p)):
            ban = banned_id[i].replace('*','.')
            if re.match(ban,p[i]) and len(ban)==len(p[i]):
                cnt+=1
        if cnt==len(banned_id):
            p = sorted(p)
            if p not in rlts:
                rlts.append(p)
    rlt = len(rlts)  
    return rlt