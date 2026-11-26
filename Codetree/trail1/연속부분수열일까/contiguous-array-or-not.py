n1,n2=map(int,input().split())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
rlt=False
for i in range(n1-n2+1):
    if a[i:i+n2]==b:
        rlt=True
        break
print("Yes" if rlt else "No")