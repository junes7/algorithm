n=int(input())
rlt=True
for i in range(2,n):
    if n%i==0:
        rlt=False
        break
print('P' if rlt else 'C')