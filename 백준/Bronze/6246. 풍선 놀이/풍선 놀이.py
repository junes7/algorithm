import sys
input=lambda:sys.stdin.readline().rstrip()
def sol(n, q):
    balloons = [1]*(n+1)
    balloons[0] = 0
    for _ in range(q):
        l, i = map(int, input().split())
        for j in range(l, n+1, i):
            balloons[j] = 0
    print(sum(balloons))
if __name__ == '__main__':
    n, q = map(int, input().split())
    sol(n, q)