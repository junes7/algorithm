n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
rlt=[0]*101
for p in segments:
    for i in range(p[0],p[1]+1):
        rlt[i]+=1
print(max(rlt))