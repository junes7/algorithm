import sys
input=lambda:sys.stdin.readline().rstrip()
while 1:
    x,y=map(int,input().split())
    if x==0 and y==0: break
    if x+y!=13:
        if x>y:
            print("To the convention.")
        elif x<y:
            print("Left beehind.")
        else:
            print("Undecided.")
    else:
        print("Never speak again.")