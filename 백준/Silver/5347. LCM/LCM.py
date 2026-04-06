from math import gcd
def lcm(x,y):
    return x*y // gcd(x,y) # 최대공약수
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    print(lcm(a,b))