def solution(line):
    if (
        len(line) == 7
        and line[0] == line[1] == line[4]
        and line[2] == line[3] == line[5] == line[6]
        and line[0] != line[6]
    ):
        return 1
    return 0
for _ in range(int(input())):
    s = input()
    print(solution(s))