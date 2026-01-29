n,m = map(int, input().split())
bulb = list(map(int,input().split()))
for i in range(m):
    inst = list(map(int, input().split()))
    if inst[0] == 1:
        bulb[inst[1]-1] = inst[2]
    elif inst[0] == 2:
        for j in range(inst[1]-1, inst[2]):
            if bulb[j] == 0:
                bulb[j] = 1
            else:
                bulb[j] = 0
    elif inst[0] == 3:
        for j in range(inst[1]-1, inst[2]):
            if bulb[j] == 1:
                bulb[j] = 0 
    elif inst[0] == 4:
        for j in range(inst[1]-1, inst[2]):
            if bulb[j] == 0:
                bulb[j] = 1 
print(*bulb)