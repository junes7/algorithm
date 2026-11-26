import sys
n = int(input())
a = [*map(int, input().split())]
min_val=min(a)
print(min_val,a.count(min_val))