# 빙고 여부를 확인할 함수 선언
def check_bingo(matrix, o_win, x_win):
    for arr in matrix:
        if "OOO" in arr:
            o_win = True
        elif "XXX" in arr:
            x_win = True
    return o_win, x_win
def solution(board):
    # O와 X의 개수를 센다.
    o_count = sum([i.count("O") for i in board])
    x_count = sum([i.count("X") for i in board])
    # O의 개수가 X보다 많거나 같을 경우 게임 종료 조건을 확인
    if 0 <= o_count - x_count <= 1:
        # O와 X의 승리 여부를 확인할 변수 선언
        o_win, x_win = False, False
        # 가로 빙고 여부 확인
        o_win, x_win = check_bingo(board, o_win, x_win)
        # board를 전치한 r_board 변수 선언
        r_board = [board[0][i]+board[1][i]+board[2][i] for i in range(3)]
        # 세로 빙고 여부 확인
        o_win, x_win = check_bingo(r_board, o_win, x_win)  
        # 대각선 표시 변수 선언
        diagonal = [board[0][0]+board[1][1]+board[2][2], board[0][2]+board[1][1]+board[2][0]]
        # 대각선 빙고 확인
        o_win, x_win = check_bingo(diagonal, o_win, x_win)  
        # 조건 확인
        # X가 이겼는데 O도 이긴 경우 0을 반환
        if x_win and o_win:
            return 0
        # O가 이겼는데 O와 X의 개수가 같은 경우 0을 반환
        elif o_win and o_count == x_count:
            return 0
        # X가 이겼는데 O의 개수가 X보다 많을 경우 0을 반환
        elif x_win and o_count > x_count:
            return 0
        # 그 외에는 정상적인 경우이므로 1을 반환
        else:
            return 1
     # O와 X의 개수 조건에 부합하지 않을 경우 0을 반환
    else:
        return 0