num = int(input())
if num == 1 or num == 2 or num == 4:
    print(0)
else:
    count = 0
    for i in range(1, num+1): #가장 짧은 변
        for j in range(i, num+1): #중간 변
            k = num - i - j #가장 긴 변
            if k >= i + j: #삼각형의 결정 조건: 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 작아야 함.
                continue
            else:
                if j > k: #중복 제거
                    break
                count += 1
    print(count)