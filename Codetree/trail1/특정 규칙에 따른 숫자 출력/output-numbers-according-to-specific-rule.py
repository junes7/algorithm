n,rlt=int(input()),1
for i in range(n):
    print(end="  "*i)
    for j in range(n-i):
        print(rlt,end=" ")
        if rlt==9:
            rlt=1
        else:
            rlt+=1
    print()
    