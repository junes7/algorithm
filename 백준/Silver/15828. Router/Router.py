from collections import deque
N = int(input())
queue = deque()
while 1:
    n = int(input())
    if n == -1:
        break
    if n != 0 and len(queue) < N:
        queue.append(n)
    elif n == 0:
        queue.popleft()
if queue:
    print(*queue)
else: 
    print("empty")