import sys
input=lambda:sys.stdin.readline().rstrip("\n")
for _ in range(int(input())):
    n = int(input())
    rlt = sum([i**2 for i in range(1, n+1)])
    print(rlt)