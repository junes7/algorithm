import math
def solution(r1, r2):
    rlt = 0
    for i in range(1,r2): #x가 정수일때 y가 정수인 점을 탐색
        y2 = math.floor(math.sqrt(math.pow(r2,2) - math.pow(i,2)))
        if i >= r1: #x값이 r1과 r2사이인 경우 
            y1 = 0
        else:		#x값이 r1보다 작은 경우
            y1 = math.ceil(math.sqrt(math.pow(r1,2) - math.pow(i,2)))
        rlt += y2-y1+1 
        
        if i >= r1:	#계산의 편의를 위해 y가 0인 x축위의 점들은 제외
            rlt -= 1     
    rlt += r2-r1+1	#x축 위에있는 점
    rlt *= 4
    return rlt