n=int(input())
rlt=[0]*3
for i in range(2,n+1):
    if i%12==0:
        rlt[2]+=1
    elif i%3==0:
        rlt[1]+=1
    elif i%2==0:
        rlt[0]+=1
print(*rlt)