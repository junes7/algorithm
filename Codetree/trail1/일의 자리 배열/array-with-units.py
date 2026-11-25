arr=[*map(int,input().split())]
for _ in range(2,10):
    arr.append((arr[-1]+arr[-2])%10)
print(*arr)