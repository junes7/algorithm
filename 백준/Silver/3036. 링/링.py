from math import gcd
n = int(input())
rings = list(map(int, input().split()))
for i in range(1, n):
    t = gcd(rings[0], rings[i])
    print(f'{rings[0] // t}/{rings[i] // t}')