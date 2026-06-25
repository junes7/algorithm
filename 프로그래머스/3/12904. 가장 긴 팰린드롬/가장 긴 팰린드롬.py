def solution(s):
    rlt = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                rlt = max(rlt, len(s[i:j]))
    return rlt