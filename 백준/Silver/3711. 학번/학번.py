import sys
input=lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())):
    stun=int(input())
    arr=[int(input()) for _ in range(stun)]
    k=1
    while True:
        rlt=set()
        for n in arr:
            rlt.add(n%k)
        if len(rlt)==stun: break
        k+=1
    print(k)