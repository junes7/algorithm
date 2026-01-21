import sys
input=lambda:sys.stdin.readline().rstrip("\n")
from itertools import combinations
num = list(map(int, input().split()))
twos = [i|j for i, j in combinations(num, 2)]
triples = [i|j|k for i, j, k in combinations(num, 3)]
rlt = 0
for i in twos:
    rlt ^= i
for j in triples:
    rlt ^= j
print(rlt)