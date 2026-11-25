n=int(input())
arr,rlt=[*map(int,input().split())],[0]*9
for i in range(n):
    rlt[arr[i]-1]+=1
print(*rlt,sep='\n')