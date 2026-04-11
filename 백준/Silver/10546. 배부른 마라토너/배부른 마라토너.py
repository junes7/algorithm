n = int(input())
part = {}
for _ in range(n):
    name = input().rstrip()
    if name in part:
        part[name] += 1
    else:
        part[name] = 1
for _ in range(n-1):
    name = input().rstrip()
    part[name] -= 1
for p in part:
    if part[p]:
        print(p)
        break