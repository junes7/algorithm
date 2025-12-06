import sys
input=lambda:sys.stdin.readline().rstrip()
m,rlt=[*map(int,input().split())],0
for i in range(int(input())):
    b,l,s=map(float,input().split())
    if l>=2.0 and s>=17:
        rlt+=m[int(b)]
print(rlt)