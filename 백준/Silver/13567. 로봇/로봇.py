import sys
input=lambda:sys.stdin.readline().rstrip()
# M, n 입력
M, n = map(int, input().split())
# 명령어 입력
orders = [input().split() for _ in range(n)]
# 방향 정의
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# 방향 상태 초기화 (동쪽)
now_direction = 0
# 위치 초기화
location = [0, 0]
# 유효 확인 플래그 정의
valid = True
# 명령어 수행
for order in orders:
    # 방향 전환 명령어라면
    if order[0] == 'TURN':
        # 왼쪽 90도 회전
        if order[1] == '0':
            now_direction = (now_direction + 1) % 4
        # 오른쪽 90도 회전
        else:
            now_direction = (now_direction - 1) % 4
    # 움직이는 명령어라면
    else:
        # 현재 방향으로 이동
        location[0] += directions[now_direction][0] * int(order[1])
        location[1] += directions[now_direction][1] * int(order[1])

        if location[0] < 0 or location[0] > M or location[1] < 0 or location[1] > M:
            # 유효하지 않음 표시
            valid = False
# 결과 출력
if not valid:
    print(-1)
else:
    print(' '.join(map(str, location)))