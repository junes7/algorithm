arr,rlt=[*map(int,input().split())],[0]*6
for i in range(10):
    rlt[arr[i]-1]+=1
for i in range(6):
    print(f"{i+1} - {rlt[i]}")