n=int(input())
rlt=1
for i in range(2,n):
    if n%i==0:
        rlt+=i
print('P' if rlt==n else 'N')