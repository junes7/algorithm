import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
channel = []
for i in range(n):
    name = input()
    if name == 'KBS1':
        idx1 = i
    elif name == 'KBS2':
        idx2 = i
    channel.append(name)
    
res = ''
res += '1' * idx1   # KBS1이 있는 곳으로 1번을 이용해서 화살표를 내린다.
res += '4' * idx1   # KBS1을 4번을 이용해서 첫 번째로 보낸다.(화살표는 첫 번째(index=0)을 가리킨다.)
if idx1 > idx2:     # KBS1이 KBS2보다 아래에 있으면 KBS1을 첫 번째로 보내는 과정을 통해 KBS2의 위치가 하나 낮아졌다.(index는 1 증가)
    idx2 += 1
res += '1' * idx2      # KBS2가 있는 곳으로 1번을 이용해서 화살표를 내린다.
res += '4' * (idx2-1)   # KBS2를 4번을 이용해서 두 번째로 보낸다.(첫 번째가 아닌 두 번째로 이동하면 되므로 idx2-1만큼 실행)
print(res)