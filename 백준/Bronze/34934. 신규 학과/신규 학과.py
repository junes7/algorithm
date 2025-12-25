import sys
input=lambda:sys.stdin.readline().rstrip()
n,rlt=int(input()),""
for i in range(n):
    sub,yr=input().split()
    if yr=='2026':
        rlt=sub
        break
print(rlt)