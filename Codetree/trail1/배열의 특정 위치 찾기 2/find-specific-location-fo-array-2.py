rlt=[0]*2
arr=list(map(int,input().split()))
for i in range(5):
    rlt[0]+=arr[2*i]
    rlt[1]+=arr[2*i+1]
print(rlt[0] - rlt[1] if rlt[0]>rlt[1] else rlt[1] - rlt[0])