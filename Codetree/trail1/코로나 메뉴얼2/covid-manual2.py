rlt=[0]*4
for _ in range(3):
    sym,temp=input().split()
    temp=int(temp)
    if sym=='Y' and temp>=37:
        rlt[0]+=1
    elif sym=='N' and temp>=37:
        rlt[1]+=1
    elif sym=='Y' and temp<37:
        rlt[2]+=1
    else:
        rlt[3]+=1
print(*rlt,'E' if rlt[0]>=2 else '')