import sys
input=lambda:sys.stdin.readline().rstrip("\n")
sup_lst={"Paper":57.99,"Printer":120.50,"Planners":31.25,"Binders":22.50,"Calendar":10.95,"Notebooks":11.20,"Ink":66.95}
rlt=0
while True:
    st=input()
    if st == "":
        break
    else:
        rlt+=sup_lst.get(st,0)
print(f"${rlt}")