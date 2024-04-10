hash_dir = [(-2, 0), (0, 2), (2, 0), (0, -2),
            (-1, -1), (1, -1), (1, 1), (-1, 1)]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(str(input()))
    board = [['.' for _ in range(len(data) * 4 + 1)] for _ in range(5)]
    idx = 5 // 2
    for i in range(2, len(board[0]), 4):
        board[idx][i] = data.pop(0)
        for j in range(8):
            nx, ny = hash_dir[j]
            nx = idx + nx
            ny = i + ny
            board[nx][ny] = '#'
    for i in range(len(board)):
        print(''.join(board[i]))