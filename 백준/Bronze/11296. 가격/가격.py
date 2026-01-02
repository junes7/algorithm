import sys
input=lambda:sys.stdin.readline().rstrip("\n")
dic={'R':0.55,'G':0.7,'B':0.8,'Y':0.85,'O':0.9,'W':0.95}
for _ in range(int(input())):
    ori,dot,vou,pri=input().split()
    ori=float(ori)
    ori*=dic[dot]
    if vou=='C':
        ori*=0.95
    ori*=100
    if pri=='C':
        if ori%10>5: ori+=10
        ori-=ori%10
    print(f"${ori/100:.2f}")