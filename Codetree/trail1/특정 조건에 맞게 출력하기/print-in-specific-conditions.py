arr=[*map(int,input().split())]
for i in range(len(arr)):
    if arr[i]==0:
        break
    if arr[i]%2==0:
        print(arr[i]//2,end=' ')
    else:
        print(arr[i]+3,end=' ')