import sys
input=lambda:sys.stdin.readline().rstrip()
rlt,chess=[0,0],{"k":0,"p":1,"n":3,"b":3,"r":5,"q":9}
for _ in range(8):
    ps = input()
    for p in ps:
        if p=='.':
            continue
        if p.isupper():
            rlt[0]+=chess[chr(ord(p)+32)]
        else:
            rlt[1]+=chess[p]
print(rlt[0]-rlt[1])