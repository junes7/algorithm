from itertools import combinations
N, K = map(int,input().split())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int,input().split())
INF  = float("INF")  #key point
def dist(c):
    b=0
    for h_idx in range(N):
        a=INF
        for c_idx in c:
            tmp = abs(x[h_idx]-x[c_idx])+abs(y[h_idx]-y[c_idx])
            a = min(a,tmp)
        b = max(b, a)
    return b 
final = INF
for c in combinations(range(N),K):
    final = min(final,dist(c))
print(final)