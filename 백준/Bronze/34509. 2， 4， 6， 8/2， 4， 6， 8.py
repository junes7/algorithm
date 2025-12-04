import sys
input=lambda:sys.stdin.readline().rstrip()
for i in range(10,99):
    st=str(i)
    if '8' not in st:
        num=ord(st[0])-48+ord(st[1])-48
        if num%6==0 and int(st[::-1])%4==0:
            print(st)
            break