arr=[[*map(int,input().split())] for i in range(2)]
tot,atot=0,0
havg,vavg=[],[]
for i in range(2):
    tot=0
    for j in range(4):
        tot+=arr[i][j]
    havg+=[f"{tot/4:.1f}"]
    atot+=tot
for j in range(4):
    tot=0
    for i in range(2):
        tot+=arr[i][j]
    vavg+=[f"{tot/2:.1f}"]
print(*havg)
print(*vavg)
print(f"{atot/8:.1f}")