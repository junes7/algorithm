t = int(input())  # 몇 번 반복할지 정수 받음
for i in range(t):
    n = int(input())  # 후보자의 수를 받음
    li = []  # 후보자들의 득표 수 넣을 리스트
    for j in range(n):
        candidate = int(input())  # 후보자의 득표수를 받고
        li.append(candidate)  # 리스트에 저장
    answer = []  # 최고 득표자가 몇명인지 확인할 리스트
    for i in range(len(li)): 
        if li[i] == max(li):
            answer.append(i)
    if len(answer) > 1:  # 만약 최다 득표자가 두명 이상이면
        print("no winner")  # 출력 후
        continue  # 밑에 코드는 실행안하고 반복문 반복
    winner = li.index(max(li)) + 1  # 최다 득표수가 들어있는 인덱스+1이 최다 득표자의 이름
    if max(li)*2 > sum(li):  # 득표수가 과반을 넘었을때
        print("majority winner {}".format(winner))
    else:  # 과반에 못넘었을때
        print("minority winner {}".format(winner))