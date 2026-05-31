def solution(maps):
    rlt = []
    w = len(maps[0])
    h = len(maps)
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    def bfs(x, y, visited):
        s = list()
        s.append((x, y))
        visited[x][y] = True
        days = 0
        while s:
            nx, ny = s.pop()
            days += int(maps[nx][ny])     
            for d in range(4):
                mx = nx + dx[d]
                my = ny + dy[d]  
                if mx < 0 or my < 0 or mx > h-1 or my > w-1:
                    continue        
                if visited[mx][my]:
                    continue        
                if maps[mx][my] == 'X':
                    continue        
                visited[mx][my] = True
                s.append((mx, my))
        return days
    visited = [[False for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'X':
                continue    
            if visited[i][j]:
                continue         
            rlt.append(bfs(i, j, visited))
    rlt.sort()
    return [-1] if len(rlt) == 0 else rlt