import sys
input=lambda:sys.stdin.readline().rstrip()
cnt=0
for i in range(int(input())):
    si,ci,ai,ri=map(int,input().split())
    if si>=1000 or ci>=1600 or ai>=1500 or 1<=ri<=30:
        cnt+=1
print(cnt)