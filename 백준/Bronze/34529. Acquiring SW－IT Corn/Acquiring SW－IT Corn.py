import sys
input=lambda:sys.stdin.readline().rstrip()
price=[*map(int,input().split())]
plan=[*map(int,input().split())]
unit,total=[100,50,20],0
for i in range(3):
    total+=plan[i]//unit[i]*price[i]
print(total)