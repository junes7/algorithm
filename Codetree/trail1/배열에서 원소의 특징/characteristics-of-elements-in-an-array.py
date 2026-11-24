arr=[*map(int,input().split())]
for i in range(10):
    if arr[i]%3==0:
        print(arr[i-1])
        break