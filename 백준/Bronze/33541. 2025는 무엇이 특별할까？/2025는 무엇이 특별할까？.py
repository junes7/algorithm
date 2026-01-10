import sys,math
input=lambda:sys.stdin.readline().rstrip("\n")
st=int(input())
while True:
    n1,n2=st//100,st%100+1
    st+=1
    if st>9999:
        print(-1)
        break
    if st==(n1+n2)**2:
        print(st)
        break