import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n,k=map(int,input().split())
a=list(map(int,input().split()))
rlt=[]
a.sort(reverse=True)
for i in range(k):
    rlt.append(a[i])
cnt,tot=0,0
for i in rlt:
    tot+=i-(len(rlt)-(len(rlt)-cnt))
    cnt+=1
print(tot)