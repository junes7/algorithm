import sys
input=lambda:sys.stdin.readline().rstrip()
N = int(input())
card = 1
if N <= 10:
    print(1)
else:
    while N >= card:
        card = str(card)
        card += '1'
        card = int(card)
    print(len(str(card//10))) #현재 card는 N보다 더 큰수이기에 10으로 나누어주어 자리 수를 구한다