import sys
input = sys.stdin.readline

r, s = map(int, input().split())
met = [input() for _ in range(r)]
data = [['.'] * s for _ in range(r)]

max_met = [-3333] * s
min_gro = [1 << 14] * s

for x in range(r):
    for y in range(s):
        if met[x][y] == 'X':
            max_met[y] = max(max_met[y], x)
        elif met[x][y] == '#':
            min_gro[y] = min(min_gro[y], x)

move = min((j - i for i, j in zip(max_met, min_gro))) - 1

for x in range(r):
    for y in range(s):
        if met[x][y] == 'X':
            data[x+move][y] = 'X'
        if met[x][y] == '#':
            data[x][y] = '#'

for i in range(r):
    for j in range(s):
        print(data[i][j], end='')
    print()