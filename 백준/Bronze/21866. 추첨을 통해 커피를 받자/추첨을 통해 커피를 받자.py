import sys
input=lambda:sys.stdin.readline().rstrip()
maxn=[100,100,200,200,300,300,400,400,500]
arr=[*map(int,input().split())]
hac,total=0,0
for i in range(9):
    if arr[i]>maxn[i]:
        hac=1
        break
    total+=arr[i]
print("hacker" if hac else "draw" if total>=100 else "none")