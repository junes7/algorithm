import sys
input=lambda:sys.stdin.readline().rstrip()
N, M = map(int, input().split())
A = list(map(int, input().split()))
level = 0
result = 0
for i in A:
    level += i
    if level < 0:  # 0보다 작으면 0으로 초기화
        level = 0
    if level >= M:  # M 이상이면 결괏값에 +1
        result += 1
print(result)