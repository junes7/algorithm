import sys
input=lambda:sys.stdin.readline().rstrip()
from heapq import heappop, heappush
n = int(input())
li = list(map(int, input().split()))
arr = []
if li[0] > 1440:
    print(-1)
    exit()
for i in li:
    heappush(arr, -i)
cnt = 0
while arr:
    if len(arr) >= 2:
        a = heappop(arr)
        b = heappop(arr)
        a += 1
        b += 1
        if a != 0:
            heappush(arr, a)
        if b != 0:
            heappush(arr, b)
    else:
        a = heappop(arr)
        a += 1
        if a != 0:
            heappush(arr, a)
    cnt += 1
if cnt > 1440:
    cnt = -1
print(cnt)