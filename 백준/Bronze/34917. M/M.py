import sys
input=lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        st=[]
        for j in range(n):
            if j==0 or j==n-1:
                st+=['#']
            else:
                st+=['.']
            if 1<=i<=n//2:
                if j==i or j==n-1-i:
                    st[j]='#'
        print(''.join(st))