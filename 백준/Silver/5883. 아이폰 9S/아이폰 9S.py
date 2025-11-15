import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
b = [int(input()) for _ in range(n)]
def ls(arr, r):
    prev = -1
    res = -1
    tmp = 0
    for i in range(n):
        if prev == arr[i]:
            tmp += 1
        elif arr[i] == r:
            continue
        else:
            prev = arr[i]
            res = max(res, tmp)
            tmp = 1
    res = max(res, tmp)
    return res
ans = -1
for r in set(b):
    ans = max(ans, ls(b, r))
print(ans)