r, c = map(int, input().split())
cp = [input() for _ in range(r)]
 
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
 
words = set()
for i in range(r):  # 행
    for j in range(c):  # 열
        # 세로
        if (i == 0 or cp[i-1][j] == '#') and cp[i][j] != '#':
            rr = i
            word = ""
            while rr < r and cp[rr][j] != '#':
                word += cp[rr][j]
                rr += 1
            if len(word) >= 2:
                words.add(word)
        # 가로
        if (j == 0 or cp[i][j-1] == '#') and cp[i][j] != '#':
            cc = j
            word = ""
            while cc < c and cp[i][cc] != '#':
                word += cp[i][cc]
                cc += 1
            if len(word) >= 2:
                words.add(word)
print(sorted(list(words))[0])