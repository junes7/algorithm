def solution(n, s):
    if s<n:
        return [-1]
    num = s//n
    rest = s%n
    rlt=[num]*n
    if rest != 0:
        for a in range(len(rlt)):
            rlt[a] += 1
            rest -= 1
            if rest == 0:
                break
    rlt.sort()
    return rlt