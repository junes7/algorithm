import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
stack = []	#현재 대기줄
maxs = [0,0]
for _ in range(n):
    info = list(map(int,input().split()))	#입력
    if len(info) == 1:	#입력이 2라면?
        stack.pop(0)	#식사가 준비되었으니 현재 대기줄 맨 앞에 있는 인원을 제거해준다
    else:	#아니라면 마지막에 줄을 세운다
        stack.append(info[1])
    if maxs[0] < len(stack):	#현재 줄에 최대 인원이 있다면 갱신해준다
        maxs[0] = len(stack)
        maxs[1] = stack[-1]
    elif maxs[0] == len(stack):	#현재 줄에 인원이 최대라면? 마지막 인원이 작은 값을 취해준다
        maxs[1] = min(maxs[1],stack[-1])
print(maxs[0],maxs[1])