def swap(i, j):
    global command
    if command == 'up' or command == 'down':
        return j, i
    return i, j


def move(command):
    data = move_dict[command]
    for a in range(data[0], data[1], data[2]):
        temp = []
        for j in range(data[3], data[4], data[5]):
            i, j = swap(a, j)
            if board[i][j]:
                temp.append(board[i][j])
                board[i][j] = 0
                
        k = 0
        while len(temp) > k + 1:
            if temp[k] == temp[k + 1]:
                temp[k] += temp[k + 1]
                temp.pop(k + 1)
            k += 1
        
        for j in range(data[3], data[4], data[5]):
            i, j = swap(a, j)
            if not temp:
                break
            board[i][j] = temp.pop(0)

t = int(input())
for test_case in range(1, t+1):
    n, command = input().split()
    n = int(n)
    board = [list(map(int, input().split())) for _ in range(n)]
    move_dict = {'up': (0, n, 1, 0, n, 1),
                'down': (n - 1, -1, -1, n - 1, -1, -1),
                'left': (0, n, 1, 0, n, 1),
                'right': (0, n, 1, n - 1, -1, -1)}
    
    move(command)
    print(f'#{test_case}')
    for b in board:
        print(*b)