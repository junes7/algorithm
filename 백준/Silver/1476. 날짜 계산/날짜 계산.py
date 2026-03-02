e, s, m = map(int, input().split())
# 연도
year = 1
# 세 수의 나머지가 모두 0이 되는 연도 찾기
while True:
    if (year-e) % 15 == 0 and (year-s) % 28 ==0 and (year-m) % 19 == 0:
        break
    year += 1
# 연도 출력
print(year)