arr,rlt=[*map(int,input().split())],[]
for i in range(len(arr)):
    if arr[i]==0:
        break
    rlt.append(arr[i])
for i in range(len(rlt),0,-1):
    print(rlt[i-1],end=' ')