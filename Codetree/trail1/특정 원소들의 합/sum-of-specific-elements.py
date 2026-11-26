arr=[[*map(int,input().split())] for _ in range(4)]
tot=0
for i in range(4):
    for j in range(i+1):
        tot+=arr[i][j]
print(tot)