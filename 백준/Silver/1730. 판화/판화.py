import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input().strip()) 
data = [['.'] * n for _ in range(n)] 
message = input().strip() 
x, y = 0, 0 
for m in message:
    if m == 'D':  # 아래로 이동
        if x + 1 < n: 
            for j in range(2):
                if data[x][y] == '-':
                    data[x][y] ='+'
                elif data[x][y] == '.':
                    data[x][y] = '|'
                if j == 0:
                    x += 1               
    elif m == 'U':  # 위로 이동
        if x - 1 >= 0: 
            for j in range(2):
                if data[x][y] == '-':
                    data[x][y] ='+'
                elif data[x][y] == '.':
                    data[x][y] = '|'
                if j == 0:
                    x -= 1
    elif m == 'L':  # 왼쪽으로 이동
        if y - 1 >= 0:  
            for j in range(2):
                if data[x][y] == '|':
                    data[x][y] ='+'
                elif data[x][y] == '.':
                    data[x][y] = '-'
                if j == 0:
                    y -= 1
    elif m == 'R':  # 오른쪽으로 이동
        if y + 1 < n: 
            for j in range(2):
                if data[x][y] == '|':
                    data[x][y] ='+'
                elif data[x][y] == '.':
                    data[x][y] = '-'
                if j == 0:
                    y += 1
for row in data:
    print(''.join(row))