import math
def solution(target):
    # dp 문제.
    # dp[i][0] = i점을 맞출 때 던질 수 있는 최소한의 다트 수
    # dp[i][1] = 그때 싱글 / 불 맞춘 횟수
    dp = [[math.inf, 0] for _ in range(target+1)]
    dp[0][0] = 0
    for i in range(1, target+1):
        # 20까지를 기준으로
        for j in range(1, 21):
            # 불 쏘는 경우            
            if i >= 50:
                # i를 불로 쏘는 게 더 적게 던지는 경우                 
                if dp[i][0] > dp[i-50][0]+1:
                    dp[i][0] = dp[i-50][0]+1
                    dp[i][1] = dp[i-50][1]+1 # 불 던지니까 +1
                # 차이가 없는 경우, 불 쐈을 때 최솟값이면 바꿔준다
                elif dp[i][0] == dp[i-50][0]+1:
                    dp[i][1] = max(dp[i-50][1]+1, dp[i][1])      
            # 싱글을 쏘는 경우
            if i >= j:
                if dp[i][0] > dp[i-j][0]+1:
                    dp[i][0] = dp[i-j][0]+1
                    dp[i][1] = dp[i-j][1]+1
                # 차이가 없는 경우, 싱글 쐈을 때 최솟값이면 바꿔준다
                elif dp[i][0] == dp[i-j][0] + 1:
                    dp[i][1] = max(dp[i][1], dp[i-j][1]+1)
            # 더블을 쏘는 경우
            if i >= j*2:
                if dp[i][0] > dp[i - (j*2)][0]+1:
                    dp[i][0] = dp[i - (j*2)][0]+1
                    dp[i][1] = dp[i - (j*2)][1]
            if i >= j*3:
                if dp[i][0] > dp[i - (j*3)][0]+1:
                    dp[i][0] = dp[i - (j*3)][0]+1
                    dp[i][1] = dp[i - (j*3)][1]
    rlt = []
    rlt.append(dp[target][0])
    rlt.append(dp[target][1])
    return rlt