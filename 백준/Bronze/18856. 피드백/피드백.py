import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n=int(input())
arr=[0]*n
arr[0],arr[1],arr[-1]=1,2,997
for i in range(1,n):
    if arr[i]==0:
        arr[i]=arr[i-1]+1
print(n)
print(*arr)