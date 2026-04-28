def solution(n, w, num):
    rlt = 0
    h = n//w+1      # 높이
    x = 1           # 상자 번호
    str = []    # 창고  
    for i in range(h):
        t = []
        for j in range(w):
            if x <= n:  # n보다 작은 상자들
                t.append(x)
                x += 1
            else:       # n보다 큰 빈 공간은 0으로
                t.append(0)
        
        if i % 2 == 0:  # 정방향 라인
            str.append(t)
        else:           # 역방향 라인
            t.reverse()
            str.append(t) 
    for i in range(len(str)):
        for j in range(len(str[0])):
            if str[i][j] == num:
                d = i
                while d < h and str[d][j]:    # 꺼낼 박스가 있으면
                    rlt += 1
                    d += 1	# 아래로 내려감
    return rlt