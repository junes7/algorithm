arr=[*map(int,input().split())]
for _ in range(2,10):
    arr+=[arr[-1]+2*arr[-2]]
print(*arr)