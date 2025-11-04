import sys
input=lambda:sys.stdin.readline().rstrip()
r, c = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(r)]
word = []
# 반복문을 통해 가로로 연속되는 단어를 찾는다.
for i in range(r):
    width_word = ""
    for j in range(c):
        # 현재 문자가 # 아니면 문자를 낱말에 더해준다.
        if graph[i][j] != "#":
            width_word += graph[i][j]
        # 현재 문자가 # 이면서 낱말의 길이가 2이상이면 낱말모음에 추가한다.
        elif len(width_word) >= 2:
            word.append(width_word)
        # 현재 문자가 # 이면서 낱말의 길이가 2 미만이라면 필요없는? 낱말이므로 "" 초기화화
        else:
            width_word = ""
    if len(width_word) >= 2:
        word.append(width_word)
# 반복문을 통해 세로로 연속되는 단어를 찾는다.
for i in range(c):
    length_word = ""
    for j in range(r):
        if graph[j][i] != "#":
            length_word += graph[j][i]
        elif len(length_word) >= 2:
            word.append(length_word)
        else:
            length_word = ""
    if len(length_word) >= 2:
        word.append(length_word)
# 사전식 순으로 정렬 후 첫 번째 낱말을 출력
word.sort()
print(word[0])