import sys
input=lambda:sys.stdin.readline().rstrip("\n")
dic={'R':0.45,'G':0.3,'B':0.2,'Y':0.15,'O':0.1,'W':0.05}
for _ in range(int(input())):
    ori,dot,vou,pri=input().split()
    ori=float(ori)
    ori*=(1-dic[dot])
    if vou=='C':
        ori*=0.95
    ori*=100
    if pri=='C':
        if ori%10>5: ori+=10
        ori-=ori%10
    print(f"${ori/100:.2f}")