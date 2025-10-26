import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
total,xor_g = 0,0
for _ in range(n):
    data = list(map(int, input().split()))
    if data[0] == 1:
        total += data[1]
        xor_g ^= data[1]
    elif data[0] == 2:
        total -= data[1]
        xor_g ^= data[1]
    elif data[0] == 3:
        print(total)
    elif data[0] == 4:
        print(xor_g)