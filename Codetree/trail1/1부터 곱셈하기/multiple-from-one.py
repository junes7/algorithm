n=int(input())
rlt=1
for i in range(1,11):
    rlt*=i
    if rlt>=n:
        print(i)
        break