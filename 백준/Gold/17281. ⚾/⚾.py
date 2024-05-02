import sys
input = sys.stdin.readline

def dfs(cnt):
    global result

    if cnt == 9:
        player = 0
        score = 0

        for inning in data:
            b1, b2, b3, out = 0, 0, 0, 0
            while out < 3:
                pos = bat[player]
                if inning[pos] == 0:
                    out += 1
                elif inning[pos] == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[pos] == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif inning[pos] == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                else:
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0

                player = (player + 1) % 9
        result = max(result, score)
        return

    # 타순 정하기
    for i in range(9):
        if check[i] == 1:
            continue
        check[i] = 1
        bat[i] = cnt

        dfs(cnt + 1)
        check[i] = 0
        bat[i] = 0


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
bat = [0 for _ in range(9)]     # 타순
check = [0 for _ in range(9)]   # 중복 검사
check[3] = 1
result =0
dfs(1)
print(result)