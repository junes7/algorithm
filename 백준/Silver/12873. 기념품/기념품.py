import sys
input=lambda:sys.stdin.readline().rstrip()
N = int(input().rstrip())
join_li = [i for i in range(1, N+1)]
t = 0
num = 0
while len(join_li) > 1:
    t += 1
    num += t**3 -1
    num = num % len(join_li)
    join_li.pop(num)
print(join_li[0])