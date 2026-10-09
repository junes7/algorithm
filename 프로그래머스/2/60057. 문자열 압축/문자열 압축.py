def solution(s):
    rlt = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        ans = ''
        tmp = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    ans += str(cnt) + tmp
                else:
                    ans += tmp
                cnt = 1
                tmp = s[j:j+i]
        if cnt > 1:
            ans += str(cnt) + tmp
        else:
            ans += tmp
        rlt.append(len(ans))
    return min(rlt)