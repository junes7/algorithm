n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)
rlt=[0]*2001
cur,cnt=1000,0
for i in range(n):
    for j in range(x[i]):
        if dir[i]=='R':
            rlt[cur+j]+=1
        else:
            rlt[cur-(j+1)]+=1
    cur=cur+x[i] if dir[i]=='R' else cur-x[i]
for c in rlt:
    if c>=2:
        cnt+=1
print(cnt)