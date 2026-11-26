arr,rlt=[*map(int,input().split())],[0]*9
i=0
while arr[i]!=0:
    if arr[i]>=10:
        rlt[arr[i]//10-1]+=1
    i+=1
for i in range(9):
    print(f"{i+1} - {rlt[i]}")