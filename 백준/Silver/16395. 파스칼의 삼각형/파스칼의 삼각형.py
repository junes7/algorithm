n,k=map(int,input().split()) #1~30
arr=[[],[1],[1,1]]
for i in range(3,n+1):
    x=[1]*i
    for j in range(1,i-1):
        x[j]=arr[i-1][j-1]+arr[i-1][j]
    arr.append(x)
print(arr[n][k-1])