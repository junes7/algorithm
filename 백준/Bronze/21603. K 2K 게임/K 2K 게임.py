import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n,k=map(int,input().split())
modk,mod2k=k%10,(2*k)%10
rlt=[]
for i in range(1,n+1):
    if i%10!=modk and i%10!=mod2k:
        rlt.append(i)
print(len(rlt))
print(*rlt)