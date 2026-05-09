from collections import deque
def solution(m, n, h, w, drops):
    rlt = []
    INF = len(drops) + 1 #끝까지 비 안맞는 칸 (최대값)
    # 각 칸이 몇번째에 젖는지 기록
    time = [[INF] * n for _ in range(m)]
    for i in range(len(drops)):
        a, b = drops[i]
        time[a][b] = i + 1
    width = n - w + 1
    row_min = [[0] * width for _ in range(m)]
    for i in range(m):
        dq = deque() # 최소값 인덱스 저장
        for j in range(n):
            # 덱 맨 뒤 값이 현재 값보다 크거나 같으면 제거 (최소값만 덱에 저장하기 위해) 
            while dq and time[i][dq[-1]] >= time[i][j]:
                dq.pop()   
            dq.append(j)
            # 슬라이드 범위 밖 인덱스 제거
            while dq and dq[0] <= j - w:
                dq.popleft()
            # 길이 w가 완성되면서부터 최소값 기록
            if j >= w - 1:
                row_min[i][j - w + 1] = time[i][dq[0]]
    #row_min 배열에서 한번 더 슬라이드-윈도우 -> rect_min에 저장
    height = m - h + 1
    rect_min = [[0] * width for _ in range(height)]
    for j in range(width):
        dq = deque()
        for i in range(m):
            while dq and row_min[dq[-1]][j] >= row_min[i][j]:
                dq.pop()       
            dq.append(i)          
            while dq and dq[0] <= i - h:
                dq.popleft()
            if i >= h - 1:
                rect_min[i - h + 1][j] = row_min[dq[0]][j]
    maxValue = -1
    rlt = [0, 0]  
    # 정답 탐색
    for i in range(height):
        for j in range(width):
            if rect_min[i][j] > maxValue:
                maxValue = rect_min[i][j]
                rlt = [i, j]    
    return rlt