dx = [1, 0, 0]
dy = [0, 1, -1]

for _ in range(1, 11):
    test_case = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    
    r = 99
    c = 0
    for i in range(100):
        if data[99][i] == 2:
            c = i

    while r != 0:
        if 0 <= c+1 < 100 and data[r][c+1]:
            while c+1 < 100 and data[r][c+1]:
                c += 1
            r -= 1

        elif 0 <= c-1 < 100 and data[r][c-1]:
            while c-1 < 100 and data[r][c-1]:
                c -= 1
            r -= 1

        else:
            r -= 1
    print(f'#{test_case} {c}')