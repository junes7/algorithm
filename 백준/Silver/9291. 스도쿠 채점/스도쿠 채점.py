import sys
input=lambda:sys.stdin.readline().rstrip()
def check_sudoku_9x9(sudoku):    
    col_count = [[1 for _ in range(9 + 1)] for _ in range(9)]   
    for i in range(9):
        row = sudoku[i]
        row_count = [1] * 10
        for j in range(9):
            col = row[j]
            row_count[col] -= 1
            col_count[j][col] -= 1
            if row_count[col] < 0:
                return False         
            if col_count[j][col] < 0:
                return False
    return True

def check_sudoku_3x3(sudoku):
    sudoku_3x3_list = [[] for _ in range(9)]
    k = 0  
    for i in range(1, 9 + 1):
        row = sudoku[i - 1]
        l = k
        for j in range(0, 9, 3):
            sudoku_3x3_list[l] += row[j:j + 3]
            l += 1        
        if i % 3 == 0:
            k += 3  
    for sudoku_3x3 in sudoku_3x3_list:
        number_count = [1] * 10
        for number in sudoku_3x3:
            number_count[number] -= 1
            if number_count[number] < 0:
                return False
    return True

T = int(input())
for t in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    if t != T:
        input()
    is_valid_sudoku_9x9 = check_sudoku_9x9(sudoku)
    is_valid_sudoku_3x3 = check_sudoku_3x3(sudoku)
    is_valid = True if is_valid_sudoku_9x9 and is_valid_sudoku_3x3 else False
    print(f'Case {t}: {"CORRECT" if is_valid else "INCORRECT"}')