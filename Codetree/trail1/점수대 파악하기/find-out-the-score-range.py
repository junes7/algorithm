arr, i, rlt = [*map(int, input().split())], 0, [0] * 10
while arr[i] != 0:
    if arr[i] >= 10:
        rlt[arr[i] // 10 - 1] += 1
    i += 1
for i in range(10, 0, -1):
    print(f"{10*i} - {rlt[i-1]}")