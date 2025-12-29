import sys,math
input=lambda:sys.stdin.readline().rstrip()
n,rlt=int(input()),[0]*2
arr=[*map(int,input().split())]
for i in range(n):
    if arr[i]%2!=0:
        rlt[0]+=1
    else:
        rlt[1]+=1
print(1 if rlt[0]==math.ceil(n/2) and rlt[1]==n//2 else 0)