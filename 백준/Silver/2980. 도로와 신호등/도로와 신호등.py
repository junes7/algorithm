N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0
pre = 0
# 초록불이 시작되는 시간에 total값이 같거나 초록불이 켜져있는 동안은 지체 시간이 없음 (간 거리만큰 시간 걸림)
for i in range(N):
    total += (arr[i][0] - pre)  # 현재점에서 그전까지 거리
    pre = arr[i][0]  # 그 전에 간 거리
    if (total % (arr[i][1] + arr[i][2])) <= arr[i][1] :  # 빨간불이 켜져있는데 도착한 경우 
        x = (total % (arr[i][1] + arr[i][2])) - arr[i][1]  # 기다려야 하는 시간 (음수)
        total += abs(x)
total += L - arr[-1][0]  # 마지막 남은 값 더해주기 -> 신호등 없으니 거리만큼 시간 걸림
print(total)