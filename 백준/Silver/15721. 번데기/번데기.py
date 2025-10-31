import sys
input=lambda:sys.stdin.readline().rstrip()
A = int(input())
T = int(input())
N = int(input())
games = [] # 게임 진행 상황 (튜플로 저장)
bbun = 1 # 뻔 을 외친 횟수
degi = 1 # 데기 를 외친 횟수
cnt = 0 # 몇번째 게임인지 
while(True):
    num = bbun # 이전 회차에서 뻔 or 데기를 외친 누적 횟수
    cnt += 1  
    # 1) 처음에 뻔 - 데기 - 뻔 - 데기 이 4번 반복은 동일함
    for _ in range(2):
        games.append((bbun, 0))
        bbun += 1
        games.append((degi, 1))
        degi +=1 
    # 2) 뻔 - 뻔 - 반복부분
    # (1): 2번, (2): 3번, (cnt): cnt+1번
    for _ in range(cnt+1):
        games.append((bbun, 0))
        bbun +=1 
    for _ in range(cnt+1):
        games.append((degi, 1))
        degi += 1
    # 3) 정답 찾기
    # 4 <= 6 < 9: 2회차에서 찾아야 함 
    if (num <= T < bbun):
        print(games.index((T, N)) % A)
        break