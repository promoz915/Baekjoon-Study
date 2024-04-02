def sudoku(n):
    for i in range(9):
        row_num = [0] * 10
        col_num = [0] * 10
        for j in range(9):
            row = n[i][j]
            col = n[j][i]
            
            if row_num[row]: return 0
            if col_num[col]: return 0
            
            row_num[row] = 1
            col_num[col] = 1
            
            if i % 3 == 0 and j % 3 == 0:
                nemo = [0] * 10
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        num = n[a][b]
                        if nemo[num]: return 0
                        nemo[num] = 1
    return 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = sudoku(arr)
    print(f'#{test_case} {ans}')