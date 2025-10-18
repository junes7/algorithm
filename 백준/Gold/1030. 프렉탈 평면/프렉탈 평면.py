s,n,k,r1,r2,c1,c2 = map(int, input().split())
size = n ** s # 프랙탈의 전체 크기
paint = (n-k) // 2 # 프랙탈 동작 시 처음 색칠하게 될 부분의 인덱스
lst = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
def recur(t,x,y,color):
    if t == 1:
        if color and r1 <= x <= r2 and c1 <= y <= c2:
            lst[x-r1][y-c1] = 1
        return
    tmp = t//n # 인덱스 뛰는 단위. 재귀를 돌 때마다 작아짐.
    for i in range(n):
        for j in range(n):
            if (r1 <= x + tmp * i <= r2) or (r1 <= x + tmp * (i+1) <= r2) or (x + tmp * i <= r1 and x + tmp * (i+1) >= r2 ): # 이것과 아래 if문은 접근 3에서 추가한 코드.
                if (c1 <= y + tmp * j <= c2) or (c1 <= y + tmp * (j+1) <= c2) or (y + tmp * j <= c1 and y + tmp * (j+1) >= c2 ):
                    if (paint <= i < paint + k) and (paint <= j < paint + k) or color: # 색칠할 곳 판정
                        recur(tmp, x + tmp * i, y + tmp * j, 1) #1을 넣으면 검게 칠할 곳
                    else:
                        recur(tmp, x + tmp * i, y + tmp * j, 0) #0을 넣으면 냅둠
recur(size, 0,0,0)
for i in lst:
    print(*i, sep='')