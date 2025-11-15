import sys
input=lambda:sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n = int(input())
    count = [0]*1001
    for _ in range(n):
        count[int(input())] += 1
    most = max(count)
    print(count.index(most))