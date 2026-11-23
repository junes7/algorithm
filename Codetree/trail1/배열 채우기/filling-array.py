arr,rlt=[*map(int,input().split())],[]
for i in range(len(arr)):
    if arr[i]==0:
        break
    rlt.append(arr[i])
print(*rlt[::-1])