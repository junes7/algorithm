def solution(key, lock):
    n, m=len(lock),len(key)
    key_li= [ [] for _ in range(4) ]
    count_key=0
    for r in range(m):
        for c in range(m):
            if key[r][c]==1:
                count_key+=1
                for i in range(4):
                    key_li[i].append([r,c])
                    t = r
                    r = c
                    c = n-t-1
    lock_li=[]
    count_lock=0
    for i in range(n):
        for j in range(n):
            if lock[i][j]==0:
                count_lock+=1
                lock_li.append([i,j])
    if count_lock==0:
        return True
    if count_lock > count_key:
        return False
    else:
        for i in range(count_lock):
            for j in range(4):
                for k in range(count_key):
                    li = []
                    x = lock_li[i][0]-key_li[j][k][0]
                    y = lock_li[i][1]-key_li[j][k][1]
                    for g in range(count_key):
                        li.append([key_li[j][g][0]+x, key_li[j][g][1]+y])
                    t=True
                    for lo in lock_li:
                        if lo not in li:
                            t=False
                            break
                        li.remove(lo)
                    for trash in li:
                        if 0 <= trash[0] < n and 0 <= trash[1] < n:
                            t=False
                    if t:
                        return True
        if t==False:
            return False