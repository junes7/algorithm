import sys; input = sys.stdin.readline

while True:
    # EOF 처리
    try:
        n = int(input())
    except:
        break

    # 숫자가 나타났는지 확인할 배열
    appear = [False] * 10

    rest = 10 # 나타나지 않은 숫자의 개수
    # n, 2n, 3n, ..., kn 형태이므로 n을 더해주면서 자리마다 숫자를 체크해주자.
    S = k = 0

    # 나타나지 않은 숫자의 개수가 0이 될 때까지
    while rest:
        k += 1
        S += n
        q = S
        while q:
            q, r = divmod(q, 10)
            if not appear[r]: # 만약 나타나지 않은 숫자이면 체크
                appear[r] = True
                rest -= 1
                if not rest: # 나타나지 않은 숫자가 없으면 탐색 중단
                    break
    print(k)