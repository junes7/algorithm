n = int(input())
arr = list(map(int, input().split()))
idx = 0
count = 1
for i in range(1, n):
    if (arr[idx] + arr[i]) % 2:
        count += 1
        idx = i
print(count)