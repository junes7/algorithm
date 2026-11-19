def solution(cmds):
    rlt = []
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    brd = [["EMPTY"] * 50 for _ in range(50)]
    for cmd in cmds:
        cmd = cmd.split(' ')
        if cmd[0] == 'UPDATE':
            if len(cmd) == 4:
                r,c,val = int(cmd[1])-1,int(cmd[2])-1,cmd[3]
                x,y = merged[r][c]
                brd[x][y] = val
            elif len(cmd) == 3:
                val1, val2 = cmd[1], cmd[2]
                for i in range(50):
                    for j in range(50):
                        if brd[i][j] == val1:
                            brd[i][j] = val2
        elif cmd[0] == 'MERGE':
            r1,c1,r2,c2 = int(cmd[1])-1, int(cmd[2])-1, int(cmd[3])-1, int(cmd[4])-1
            x1,y1 = merged[r1][c1]
            x2,y2 = merged[r2][c2]
            if brd[x1][y1] == "EMPTY":
                brd[x1][y1] = brd[x2][y2]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2,y2):
                        merged[i][j] = (x1,y1)
        elif cmd[0] == 'UNMERGE':
            r, c = int(cmd[1])-1,int(cmd[2])-1
            x, y = merged[r][c]
            tmp = brd[x][y]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x,y):
                        merged[i][j] = (i,j)
                        brd[i][j] = "EMPTY"
            brd[r][c] = tmp
        elif cmd[0] == 'PRINT':
            r, c = int(cmd[1])-1, int(cmd[2])-1
            x, y = merged[r][c]
            rlt.append(brd[x][y])
    return rlt