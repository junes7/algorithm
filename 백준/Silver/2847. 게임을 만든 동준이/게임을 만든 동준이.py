import sys
input=lambda:sys.stdin.readline().rstrip()
n,points,rlt = int(input()),[],0
for _ in range(n):
    points.append(int(input()))
points.reverse()
for i in range(1,n):
    if points[i] >= points[i-1]:
        dif = points[i] - points[i-1] + 1
        points[i] -= dif
        rlt += dif
        dif = 0
print(rlt)