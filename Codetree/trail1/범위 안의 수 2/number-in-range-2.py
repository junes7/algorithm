rlt=[]
for _ in range(10):
    e=int(input())
    if e>=0 and e<=200:
        rlt+=[e]
print(sum(rlt),f"{sum(rlt)/len(rlt):.1f}")