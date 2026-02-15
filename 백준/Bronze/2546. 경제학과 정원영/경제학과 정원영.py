T = int(input())
for t in range(T):
    empty_line = input()
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    Economics = list(map(int, input().split()))
    # 평균
    C_avg = sum(C) / N
    Economics_avg = sum(Economics) / M
    result = 0
    # C언어 평균보다 낮고 경제학 원론 평균보다 높은 수강생 찾기
    for c in C:
        if c < C_avg and c > Economics_avg:
            result += 1
    print(result)