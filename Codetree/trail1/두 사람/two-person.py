p1=input().split()
p1age=int(p1[0])
p2=input().split()
p2age=int(p2[0])
if (p1age>=19 and p1[1]=='M') or(p2age>=19 and p2[1]=='M'):
    print(1)
else:
    print(0)