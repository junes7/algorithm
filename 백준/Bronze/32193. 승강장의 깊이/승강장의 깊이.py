N = int(input())
platform = [0]  # 원본 배열
S = [0] * (N + 1)  # 누적합 배열
for _ in range(N):
    A, B = map(int, input().split())
    platform.append(A - B)
for k in range(1, N + 1):
    S[k] = S[k - 1] + platform[k]
for i in S[1:]:
    print(i)