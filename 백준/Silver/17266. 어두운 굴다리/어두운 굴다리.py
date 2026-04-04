import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n = int(input())
m = int(input())
location = list(map(int, input().split()))
length = 0
if m == 1:
    length = max(location[0], n - location[0])
else:
    for i in range(m):
        if i == 0:
            x = location[i]
        elif i == m-1:
            x = n - location[i]
        else:
            distance = location[i] - location[i-1]
            if distance % 2 == 0:
                x = distance // 2
            else:
                x = distance // 2 + 1
        length = max(x, length)
print(length)