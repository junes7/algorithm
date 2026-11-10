a,b=map(int,input().split())
rlt=0
for i in range(a,b+1):
    if i%6==0 and i%8!=0:
        rlt+=i
print(rlt)