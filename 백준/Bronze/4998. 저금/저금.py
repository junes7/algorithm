import sys
input=lambda:sys.stdin.readline().rstrip()
try:
    while(1):
        n, b, m = map(float, input().split())
        cnt = 0
        while (n < m):
            n += n*(b/100)
            cnt += 1
        print(cnt)    
except:
    exit()