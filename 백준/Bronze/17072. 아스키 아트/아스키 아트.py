import sys
input=lambda:sys.stdin.readline().rstrip()
def calc_intensity(R, G, B):
    return (2126 * R) + (7152 * G) + (722 * B)
def formatted_char(intensity):
    if 2040000 <= intensity:
        return '.'
    elif 1530000 <= intensity:
        return '-'
    elif 1020000 <= intensity:
        return '+'
    elif 510000 <= intensity:
        return 'o'
    elif 0 <= intensity:
        return '#'
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    line = map(int, sys.stdin.readline().split())
    formatted_line = ''
    r, g, b = 0, 0, 0
    for i, v in enumerate(line, 1):
        if i % 3 == 1:
            r = v
        elif i % 3 == 2:
            g = v
        elif i % 3 == 0:
            b = v
            formatted_line += formatted_char(calc_intensity(r, g, b))  
    print(formatted_line)