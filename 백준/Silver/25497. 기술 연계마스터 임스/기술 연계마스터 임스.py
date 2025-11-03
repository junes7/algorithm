import sys
input=lambda:sys.stdin.readline().rstrip()
N = int(input())
skill = input()
cnt = 0	# 사용한 기술 총 횟수
Ls, Ss = 0, 0	# 사전 기술 L,S 의 사용 횟수
for i in skill :
    if i == 'L' :	# 사전 기술 L
        Ls += 1
    elif i == 'R' :	# 본 기술 R
        if Ls > 0 :	# L의 사용 횟수가 0보다 크면
            cnt += 1	# 총 횟수 +1
            Ls -= 1	# L의 횟수 -1
        else :		# 그게 아니라면 break
            break	
    elif i == 'S' :	# 사전 기술 S
        Ss += 1
    elif i == 'K' :	# 본 기술 K
        if Ss > 0 :	# S의 사용 횟수가 0보다 크면
            cnt += 1	# 총 횟수 +1
            Ss -= 1	# S의 횟수 -1
        else :		# 그게 아니라면 break
            break
    else :	# 1~9의 기술
        cnt += 1 
print(cnt)