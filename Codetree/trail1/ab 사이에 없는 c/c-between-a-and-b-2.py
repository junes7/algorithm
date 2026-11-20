arr=input().split()
a,b,c=int(arr[0]),int(arr[1]),int(arr[2])
rlt=True
for i in range(a,b+1):
    if i%c==0:
        rlt=False
        break
print("YES" if rlt else "NO")