move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
command_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S': 4,
                '^': 0, 'v': 1, '<': 2, '>': 3,
                0: '^', 1: 'v', 2: '<', 3: '>'}
search_list = ['<', '>', '^', 'v']

t = int(input())
for test_case in range(1, t+1):
    h, w = map(int, input().split())
    map_list = [list(input()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if map_list[i][j] in search_list:
                tank_dir = (i, j, command_dict[map_list[i][j]])
                break
        else:
            continue
        break

    n = int(input())
    order = list(input())

    for i in order:
        temp = command_dict[i]
        if temp == 4:
            dy = tank_dir[0]
            dx = tank_dir[1]
            while True:
                dy += move_list[tank_dir[2]][0]
                dx += move_list[tank_dir[2]][1]

                if 0 > dy or dy >= h or 0 > dx or dx >= w or map_list[dy][dx] == '#':
                    break
                if map_list[dy][dx] == '*':
                    map_list[dy][dx] = '.'
                    break

        else:
            y = tank_dir[0]
            x = tank_dir[1]
            dy = y + move_list[temp][0]
            dx = x + move_list[temp][1]
            map_list[y][x] = command_dict[temp]
            tank_dir = (y, x, temp)

            if 0 <= dy < h and 0 <= dx < w and map_list[dy][dx] == '.':
                map_list[y][x] = '.'
                map_list[dy][dx] = command_dict[temp]
                tank_dir = (dy, dx, temp)

    print(f'#{test_case}', end=' ')
    for i in range(h):
        print(''.join(map_list[i]))