data = [list(map(int, input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

bingo, cnt = 0, 0
check_row, check_col, check_dia = [False] * 5, [False] * 5, [False] * 2


def check(data):
    global bingo, check_dia
    right, reverse = 0, 0

    for i in range(5):
        if str(data[i]).count('[0, 0, 0, 0, 0') and not check_row[i]:
            bingo += 1
            check_row[i] = True

        col = list(map(lambda x: x[i], data))
        if str(col).count('[0, 0, 0, 0, 0]') and not check_col[i]:
            bingo += 1
            check_col[i] = True

        right += data[i][i]
        reverse += data[i][5 - i - 1]

    if not right and not check_dia[0]:
        check_dia[0] = True
        bingo += 1

    if not reverse and not check_dia[1]:
        check_dia[1] = True
        bingo += 1

    return bingo


for target in range(25):
    for i in range(5):
        for j in range(5):
            if mc[target] == data[i][j]:
                data[i][j] = 0
                cnt += 1
                check(data)
                if bingo >= 3:
                    print(cnt)
                    exit()