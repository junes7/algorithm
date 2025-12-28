import sys,math
input=lambda:sys.stdin.readline().rstrip()
n,st,cnt=input(),"",0
l=len(n)
for i in range(l-1,-1,-1):
    if cnt-3==0:
        st+=','
        cnt=0
    st+=n[i]
    cnt+=1
print(st[::-1])