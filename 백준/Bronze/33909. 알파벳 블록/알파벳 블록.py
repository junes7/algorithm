import sys
input=lambda:sys.stdin.readline().rstrip("\n")
arr=[*map(int,input().split())]
arr[1]+=arr[2]*2
arr[0]+=arr[3]
print(min(arr[0]//3,arr[1]//6))