import sys
input=lambda:sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    teamNum, gameNum = map(int,input().split())
    teamsScore = [0 for i in range(0,teamNum)]
    teamsLosePoint = [0 for i in range(0,teamNum)]
    W = [0 for i in range(0,teamNum)]
    for _ in range(gameNum):
        a,b,p,q = map(int, input().split())
        teamsScore[a-1] += p
        teamsLosePoint[a-1] += q
        teamsScore[b-1] += q
        teamsLosePoint[b-1] += p
    for i in range(teamNum):
        if teamsScore[i]**2+teamsLosePoint[i]**2 == 0:
            W[i]=0
        else:
            W[i] = (teamsScore[i]**2)/(teamsScore[i]**2+teamsLosePoint[i]**2)
    print(int(max(W)*1000))
    print(int(min(W)*1000))