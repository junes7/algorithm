import sys
input = sys.stdin.readline
num = input().rstrip()
total = 0
target = -1
for i in range(13):
    # 훼손된 숫자를 찾으면 위치 기록
    if num[i] == '*':
        target = i
        continue
    # 짝수면 가중치가 1, 홀수면 가중치가 3
    weight = 1 if i % 2 == 0 else 3
    total += int(num[i]) * weight
weight = 1 if target % 2 == 0 else 3
for i in range(10):
    if (total + i * weight) % 10 == 0:
        print(i)
        break