# 성적표 출력(print transcript)
# 세종이는 정보과학 선생님인 JH를 도와주기 위해 정보과학 성적처리 프로그램을
# 만들기로 했다. JH 선생님은 학생들의 명단과 점수를 입력하면 상위 m명의 학생
# 명단을 출력해 주기를 원한다. 다음 조건을 만족하는 프로그램을 작성해 보자.
# 첫째 줄에 데이터의 개수 n (3<=n<=100)과 출력인원 m (1<=m<=n)이 공백으로
# 구분되어 입력된다. 둘째 줄부터 학생 이름과 점수(0 100)가 공백으로 구분되어
# 입력된다. 단 이름의 길이는 최대 10바이트 이내이다.
# 상위 m명의 학생명단을 출력한다. 단, 출력순서는 점수가 높은 학생이 먼저
# 출력되며, 점수가 같을 경우 입력 순서가 빠른 순서로 출력한다.
# method 1
n, m = map(int, input().split())
d = []
for i in range(n):
    name, score = input().split()
    d.append([name, int(score)])
d = sorted(d, key=lambda x : x[1], reverse=True)
for i in range(m):
    print(d[i][0])