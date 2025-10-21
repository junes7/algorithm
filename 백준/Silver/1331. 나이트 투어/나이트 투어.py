import sys
input=lambda:sys.stdin.readline().rstrip()
def check_valid(now, dest):
    if abs(ord(now[0]) - ord(dest[0])) == 2 and abs(int(now[1]) - int(dest[1])) == 1:
        return 1
    elif abs(ord(now[0]) - ord(dest[0])) == 1 and abs(int(now[1]) - int(dest[1])) == 2:
        return 1
    else:
        return 0
sqrs = []
now = input()
sqrs.append(now)
cnt = 1
for i in range(35):
    dest = input()
    sqrs.append(dest)
    if check_valid(now,dest) == 1:
        cnt += 1
        now = dest
    else:
        break
if cnt == 36 and len(set(sqrs))== 36 and check_valid(sqrs[0],sqrs[-1]):
    print('Valid')
else:
    print('Invalid')