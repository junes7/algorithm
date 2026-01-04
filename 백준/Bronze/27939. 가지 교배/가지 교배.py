import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
type=input().split()
m,k=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(m)]
for c in arr:
    for j in c:
        if type[j-1]=='P':
            break;
    else:
        print("W")
        break
else:
    print("P")