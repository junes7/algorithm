import sys
input=lambda:sys.stdin.readline().rstrip()
from collections import deque
convert = lambda x: (x + 2) % 4 if x != 2 else 4
n = int(input())
data = deque(map(int, input().split()))
rev_data = deque(map(convert, data))
rev_data.reverse()
count = 0
result = []
for _ in range(int(input())):
    cur = deque(map(int, input().split()))
    tmp = cur.copy()
    for _ in range(n):
        if data == tmp or rev_data == tmp:
            count += 1
            result.append(cur)
        tmp.rotate(1)
print(count)
for result_list in result:
    print(*result_list)