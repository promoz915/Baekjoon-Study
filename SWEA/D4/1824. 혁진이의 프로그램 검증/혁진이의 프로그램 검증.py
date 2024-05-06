dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def func(data, visited, test_case, r, c):
    stack = [[0, 0, 1, 0]]
    while stack:
        x, y, d, m = stack.pop()
        if visited[x][y][d][m] == test_case:
            continue
        else:
            visited[x][y][d][m] = test_case
            if data[x][y] == '<' or (data[x][y] == '_' and m != 0):
                stack.append([(x + dx[0]) % r, (y + dy[0]) % c, 0, m])
            elif data[x][y] == '>' or (data[x][y] == '_' and m == 0):
                stack.append([(x + dx[1]) % r, (y + dy[1]) % c, 1, m])
            elif data[x][y] == '^' or (data[x][y] == '|' and m != 0):
                stack.append([(x + dx[2]) % r, (y + dy[2]) % c, 2, m])
            elif data[x][y] == 'v' or (data[x][y] == '|' and m == 0):
                stack.append([(x + dx[3]) % r, (y + dy[3]) % c, 3, m])
            elif data[x][y] == '@':
                return True
            elif data[x][y] == '+':
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, (m + 1) % 16])
            elif data[x][y] == '-':
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, (m - 1) % 16])
            elif data[x][y] == '.':
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, m])
            elif data[x][y] == '?':
                for i in range(4):
                    stack.append([(x + dx[i]) % r, (y + dy[i]) % c, i, m])
            else:
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, int(data[x][y])])
    return False


visited = [[[[0 for _ in range(16)] for _ in range(4)] for _ in range(20)] for _ in range(20)]
t = int(input())
for test_case in range(1, t+1):
    r, c = map(int, input().split())
    data = [input() for _ in range(r)]
    ans = func(data, visited, test_case, r, c)
    if ans:
        ans = 'YES'
    else:
        ans = 'NO'
    print(f'#{test_case} {ans}')
