import sys
input=lambda:sys.stdin.readline().rstrip()
S = input()
frame_list = [[] for _ in range(5)]
for i in range(1, len(S) + 1):
    C = S[i - 1]
    E = '*' if i % 3 == 0 else '#'
    frame = [
        f'..{E}..',
        f'.{E}.{E}.',
        f'{E}.{C}.{E}',
        f'.{E}.{E}.',
        f'..{E}..'
    ]
    for j in range(5):
        f = frame[j]
        if E == '#' and i < len(S):
            f = f[:-1]
        if 0 < i - 1 and (i - 1) % 3 == 0:
            f = f[1:]
        frame_list[j].append(f)
for row in frame_list:
    print(''.join(row))