import sys
input=lambda:sys.stdin.readline().rstrip()
n,d=map(int,input().split())
for _ in range(n):
    st=[*input()]
    for i in range(n):
        if st[i]=='d':
            st[i]='q' if d==1 else 'b'
        elif st[i]=='b':
            st[i]='p' if d==1 else 'd'
        elif st[i]=='q':
            st[i]='d' if d==1 else 'p'
        else:
            st[i]='b' if d==1 else 'q'
    print(''.join(st))