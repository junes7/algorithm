import sys
input=lambda:sys.stdin.readline().rstrip("\n")
h,y=map(int,input().split())
rlt=[h]+[0]*y
for i in range(1,y+1):
    for j in [1,3,5]:
        if i-j<0:break
        rlt[i]=max(rlt[i],int(rlt[i-j]*(1.05 if j==1 else 1.2 if j==3 else 1.35)))
print(rlt[-1])