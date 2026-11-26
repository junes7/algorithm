a,b=map(int,input().split())
rlt,tot=[0]*10,0
while a>1:
    rlt[a%b]+=1
    a//=b
for i in range(10):
    if rlt[i]!=0:
        tot+=rlt[i]**2
print(tot)