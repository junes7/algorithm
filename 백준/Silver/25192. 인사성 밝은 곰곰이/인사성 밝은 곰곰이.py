n = int(input())
gom = set()
cnt = 0
for _ in range(n):
    user = input().strip()
    if user == 'ENTER':
        cnt += len(gom)
        gom = set()
    else:
        gom.add(user)
cnt += len(gom)
print(cnt)