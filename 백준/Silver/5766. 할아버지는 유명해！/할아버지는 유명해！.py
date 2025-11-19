import sys 
input = lambda:sys.stdin.readline().rstrip()
def solve():  
    while True:  
        N, M = map(int, input().split())  
        if not N and not M:  
            break  
        ranking = [0] * 10001  
        for _ in range(N):  
            for i in list(map(int, input().split())):  
                ranking[i] += 1  

        total = sorted(set(ranking), reverse=True)  
        second = total[1]  
        for i, j in enumerate(ranking):  
            if j == second:  
                print(i, end=' ')  
        print()  
if __name__ == '__main__':  
    solve()