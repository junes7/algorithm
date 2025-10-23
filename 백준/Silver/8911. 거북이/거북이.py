import sys
input=lambda:sys.stdin.readline().rstrip()
T = int(input())
test_cases = [(input()) for _ in range(T)]
direction = {'E': [1, 0], 'W': [-1, 0], 'S': [0, -1], 'N': [0, 1]}
order = {'F': 1, 'B': -1, 'L': ['N', 'W', 'S', 'E'], 'R': ['N', 'E', 'S', 'W']}
# 이동한 경로 구하기
def move_turtle(test_case):
    turtle_x = 0
    turtle_y = 0
    turtle_state = 'N'
    sequence = [[0, 0]]
    for tc in test_case:
        if tc == 'F' or tc == 'B':
            x = direction[turtle_state][0] * order[tc]
            y = direction[turtle_state][1] * order[tc]
            turtle_x += x
            turtle_y += y
            sequence.append([turtle_x, turtle_y])
        else:
            index = order[tc].index(turtle_state) # 인덱스
            turtle_state = order[tc][(index + 1) % 4]
    return sequence
# 면적 구하기
def get_area(sequence):
    width = list(zip(*sequence))[0]
    height = list(zip(*sequence))[1]
    area = abs(max(width) - min(width)) * abs(max(height) - min(height))
    return area
# 정답 출력
for tc in test_cases:
    sequence = move_turtle(tc)
    print(get_area(sequence))