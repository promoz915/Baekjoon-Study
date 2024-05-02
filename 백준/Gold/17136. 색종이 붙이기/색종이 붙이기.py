def attach(x, y, cnt):
    global result

    # 아래로 먼저 진행
    if y >= 10:    # 탐색 종료
        result = min(result, cnt)
        return
    if x >= 10:
        attach(0, y+1, cnt)
        return

    # 덮여야 할 위치 찾기
    if board[x][y] == 1:
        for r in range(4, -1, -1):          # 색종이 큰 것 부터 적용
            if paper_amount[r] == 0:
                continue
            if x + r >= 10 or y + r >= 10:
                continue

            # 덮는 위치에 0이 있을 경우 빠져 나오기
            flag = 0
            for i in range(x, x+r+1):
                for j in range(y, y+r+1):
                    if board[i][j] == 0:
                        flag = 1
                        break
                if flag == 1:
                    break

            if flag == 0:
                # 덮은 위치 0으로 채우기
                for i in range(x, x+r+1):
                    for j in range(y, y+r+1):
                        board[i][j] = 0

                # 갯수 하나 까고 재귀 후 다시 복구
                paper_amount[r] -= 1
                attach(x+r+1, y, cnt+1)
                paper_amount[r] += 1
                for i in range(x, x+r+1):
                    for j in range(y, y+r+1):
                        board[i][j] = 1
                        
    # 안 덮어도 되면 탐색 진행
    else:
        attach(x+1, y, cnt)


board = [list(map(int, input().split())) for _ in range(10)]
paper_amount = [5, 5, 5, 5, 5]
result = 1e9
attach(0, 0, 0)

print(-1) if result == 1e9 else print(result)