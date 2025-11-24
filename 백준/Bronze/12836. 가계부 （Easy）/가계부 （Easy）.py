import sys
input=lambda:sys.stdin.readline().rstrip()
def solve():
    N, Q = map(int, input().split())
    money = [0] * (N + 1) # 살아온 날마다의 수입이나 지출
    for _ in range(Q):
        query, p, q = map(int, input().split())
        if query == 1: # 1번 쿼리
            money[p] += q
        else: # 2번 쿼리
            print(sum(money[p:q + 1]))
solve()