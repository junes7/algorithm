a,b=map(int,input().split())
if a>b:
    a,b=b,a
rlt=0
for i in range(a,b+1):
    if i%5==0:
        rlt+=i
print(rlt)