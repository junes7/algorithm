from collections import Counter
def solution(a):
    elements = Counter(a)
    rlt = -1
    for key in elements.keys():
        if elements[key] <= rlt:
            continue
        idx = 0
        cnt = 0
        while idx < len(a) - 1:
            if (a[idx] != key) and (a[idx + 1] != key):#교집합이 생기지 않음
                idx += 1
                continue
            if (a[idx] == a[idx + 1]):#조건에 위배됨
                idx += 1
                continue
            cnt += 1
            idx += 2
        rlt = max(rlt,cnt)
    if rlt == -1:
        return 0
    else:
        return rlt * 2