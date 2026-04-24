from itertools import combinations
n, m, k = map(int, input().split())
winning = 0
for case in combinations([x for x in range(n)],m):
    count = 0
    for i in range(m):
        if case[i] < m:
            count += 1
    if count >= k:
        winning += 1
print(winning/len(list(combinations([x for x in range(n)],m))))