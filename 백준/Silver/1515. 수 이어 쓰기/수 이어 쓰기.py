import sys
input=lambda:sys.stdin.readline().rstrip()
n = input()
ans = 0 #최솟값변수 
while True:
    ans += 1
    num = str(ans) #각숫자별로 비교하기 때문에 문자로 변환
    while len(num) > 0 and len(n) > 0:
        if num[0] == n[0]:
            n = n[1:]
        num = num[1:]
    if n == '':
        print(ans)
        break