import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input().rstrip()) #주어진 돈
chart = list(map(int, input().rstrip().split())) #주식 정보
BNP = [n, 0] #준현 돈, 주식 수
TIMING = [n, 0] #상민 돈, 주식 수
for i in range(len(chart)): #준현
    BNP[1] += (BNP[0] // chart[i]) #살 수 있는 만큼 사기 
    BNP[0] -= (BNP[0] // chart[i] * chart[i]) #주식 사고 남은 돈
for i in range(11): #성민
    check = chart[i:i+4]
    check_up = 0
    check_down = 0
    for j in range(3):
        if check[j+1] > check[j]: #상승 체크
            check_up+=1
        if check[j+1] < check[j]: #하락 체크
            check_down+=1
    if check_down == 3: #3일 연속 상승이면 전량매수
        TIMING[1] += (TIMING[0] // chart[i+3]) 
        TIMING[0] -= (TIMING[0] // chart[i+3] * chart[i+3])
    elif check_up == 3: #3일 연속 하락이면 전량매도
        TIMING[0] += (TIMING[1] * chart[i+3])
        TIMING[1] = 0
BNP = chart[13] * BNP[1] + BNP[0] #준현 총 금액
TIMING = chart[13] * TIMING[1] + TIMING[0] #성민 총 금액
if BNP>TIMING:
    print("BNP")
elif BNP < TIMING:
    print("TIMING")
else:
    print("SAMESAME")