from typing import List
MOD = 10007
def solution(n: int, tops: List[int]) -> int:
    a = [0 for _ in range(n)]   # a[k] : k번째 아래 방향 정삼각형을 3번 방법으로 덮은 경우의 수
    b = [0 for _ in range(n)]   # b[k] : k번째 아래 방향 정삼각형을 1, 2, 4번 방법으로 덮은 경우의 수
    a[0] = 1
    b[0] = 3 if tops[0] else 2
    for k in range(1, n):
        if tops[k]:
            a[k] = a[k-1] + b[k-1]          # 이전 방법에 대한 경우의 수에 대해 모두 3 적용 가능
            b[k] = a[k-1] * 2 + b[k-1] * 3  # 이전 방법이 3인 경우 1, 4 적용 가능 + 이전 방법이 3이 아닌 경우 1, 2, 4 적용 가능
        else:
            a[k] = a[k-1] + b[k-1]          # 이전 방법에 대한 경우의 수에 대해 모두 3 적용 가능
            b[k] = a[k-1] + b[k-1] * 2      # 이전 방법이 3인 경우 4 적용 가능 + 이전 방법이 3이 아닌 경우 2, 4 적용 가능
        a[k] %= MOD     # 주의. 매 연산마다 MOD해주지 않으면 TLE
        b[k] %= MOD
    return (a[-1]+b[-1]) % MOD