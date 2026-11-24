arr,rlt=[*map(int,input().split())],[]
for i in range(len(arr)):
    if arr[i]==0:
        break
    rlt+=[arr[i]]
print(sum(rlt[-1:-4:-1]))