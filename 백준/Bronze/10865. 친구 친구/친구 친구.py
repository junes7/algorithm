import sys
input=lambda:sys.stdin.readline().rstrip()
n,m=map(int,input().split())
dic=dict(zip([i for i in range(1,n+1)],[0]*n))
for i in range(m):
    a,b=map(int,input().split())
    dic[a]+=1
    dic[b]+=1
print(*dic.values(),sep="\n")