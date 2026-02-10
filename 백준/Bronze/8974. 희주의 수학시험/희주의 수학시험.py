A, B = map(int, input().split())
li = []
t = cnt = 1
for _ in range(B):
    li.append(t)
    if t == cnt:
        cnt = 0
        t += 1
    cnt += 1
print(sum(li[A-1:B]))