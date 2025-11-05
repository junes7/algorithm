import sys
input=lambda:sys.stdin.readline().rstrip()
N, X = map(int, input().split())
T = list(map(int, input().split()))
check = True	# while문 제어 변수
while check :
    for i in range(N) :
        if X <= T[i] :	# 목소리의 크기가 상한선 이하일 경우
            X += 1
        else :	# 그렇지 않은 경우
            result = i	# 인덱스 값 저장
            check = False	# while문 중지를 위한 False
            break	# 반복문 탈출
print(result+1)	# 인덱스+1 값이 벌칙 받는 사람