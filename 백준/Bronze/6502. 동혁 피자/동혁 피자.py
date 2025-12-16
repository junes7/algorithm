import sys,math
input=lambda:sys.stdin.readline().rstrip()
cnt=1
while 1:
    val=input()
    if val=='0': break
    r,w,l=map(int,val.split())
    pizza=math.sqrt(w**2+l**2)
    print(f"Pizza {cnt} {'fits' if 2*r>=pizza else 'does not fit'} on the table.")
    cnt+=1