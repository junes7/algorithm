n=int(input())
rlt=0
for i in range(1,101):
    rlt+=i
    if rlt>=n:
        print(i)
        break