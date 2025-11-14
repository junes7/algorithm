import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
nList = list(map(int, input().split()))
ans = 0
cnt = 0
menu = [False] * 111111
for num in nList:
    if not menu[num]:  # 한번도 안 나왔다면
        cnt += 1
        menu[num] = True
    else:
        cnt -= 1
        menu[num] = False
    ans = max(ans, cnt)  # 붙어있는 스티커 최대 개수 업데이트
print(ans)