firstN = int(input())
result = []
for second in range(1, 30000 + 1):
    temp = [firstN, second]  # temp 리스트에 첫번째 수와 2번째 수를 넣는다.
    firstN_temp = firstN  # 입력받은 값을 임시 변수에 저장
    while True:  # 반복문을 돈다.
        third = firstN_temp - second  # 3번째 이후값부터 저장
        if third < 0:  # 만약 그 값이 음수가 되면
            break  # 탈출
        temp.append(third)  # 3번째 이상의 값을 temp라는 임시 리스트에 넣는다.
        firstN_temp = second  # 두번째 값을 첫번째 값으로 바꿔주고
        second = third  # 세번째 값을 두번째 값으로 바꿔준다.

    if len(result) < len(temp):  # 만약 while문을 다돌고 나서 현재 저장된 result값보다 길이가 길다면
        result = []  # 현재 저장된 값들을 지워주고
        result += temp  # 새로운 값을 저장해준다.
print(len(result))
print(*result)