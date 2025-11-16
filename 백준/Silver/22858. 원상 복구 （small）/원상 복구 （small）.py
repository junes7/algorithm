import sys
input=lambda:sys.stdin.readline().rstrip()
n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))
p = [0 for _ in range(n)]
for _ in range(k):
    for j in range(n):
        p[d[j]-1] = s[j]
    s = list(p)
print(*p)