import sys
input=lambda:sys.stdin.readline().rstrip()
comp=[[30,40],[35,30],[40,20]]
while True:
    c,d=map(int,input().split())
    if c==0 and d==0: break
    rlt=[c*el[0]+d*el[1] for el in comp]
    print(min(rlt))