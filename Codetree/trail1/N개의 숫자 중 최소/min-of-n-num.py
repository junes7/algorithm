import sys
n = int(input())
a = [*map(int, input().split())]
min_val=sys.maxsize
for i in range(n):
    if min_val>a[i]:
        min_val=a[i]
print(min_val,a.count(min_val))