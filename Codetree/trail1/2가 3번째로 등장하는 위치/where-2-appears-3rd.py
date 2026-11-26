n, cnt = int(input()), 0
arr = [*map(int, input().split())]
for i in range(n):
    if arr[i] == 2:
        cnt += 1
    if cnt == 3:
        print(i + 1)
        break