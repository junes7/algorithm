n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
m = min(segments)[0]
m = abs(m) if m < 0 else 0
rlt = [0] * 201
for i in range(n):
    st, end = segments[i][0] + m, segments[i][1] + m
    for j in range(end - st):
        rlt[st + j] += 1
print(max(rlt))