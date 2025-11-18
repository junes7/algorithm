import sys
input=lambda:sys.stdin.readline().rstrip()
start_1, ans_1 = [0, 1, 0, 0], 0
start_2, ans_2 = [0, 0, 1, 0], 0
start_3, ans_3 = [0, 0, 0, 1], 0
N = int(input())
for i in range(N):
    a, b, g = map(int, input().split())
    start_1[a], start_1[b] = start_1[b], start_1[a]
    start_2[a], start_2[b] = start_2[b], start_2[a]
    start_3[a], start_3[b] = start_3[b], start_3[a]
    if start_1[g] == 1:
        ans_1 += 1
    if start_2[g] == 1:
        ans_2 += 1
    if start_3[g] == 1:
        ans_3 += 1
print(max(ans_1, ans_2, ans_3))