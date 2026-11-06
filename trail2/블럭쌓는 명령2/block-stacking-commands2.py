n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
rlt=[0]*(n+1)
for i in range(k):
    for j in range(commands[i][1]-commands[i][0]+1):
        rlt[commands[i][0]+j]+=1
print(max(rlt))