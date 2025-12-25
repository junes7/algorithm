import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
arr=[*map(int,input().split())]
rlt=True
for i in range(n-1):
    if arr[i]>=arr[i+1]:
        rlt=False
        break
print(1 if rlt else 0)