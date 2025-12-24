import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
arr=[int(input()) for i in range(n)]
rlt,prev=0,arr[0]
for i in range(1,n):
    if prev>=arr[i]:
        prev=arr[i]
    else:
        rlt+=arr[i]-prev
print(rlt)