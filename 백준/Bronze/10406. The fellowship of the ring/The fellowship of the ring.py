import sys
input=lambda:sys.stdin.readline().rstrip("\n")
w, n, p = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
for h in li:
    if w <= h <= n:
        cnt += 1
print(cnt)