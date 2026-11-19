n=int(input())
rlt=False
for i in range(2,n):
    if n%i==0:
        rlt=True
        break
print('C' if rlt else 'N')