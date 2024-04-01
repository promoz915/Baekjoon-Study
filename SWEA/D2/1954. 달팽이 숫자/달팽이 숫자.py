T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for i in range(n)]
    
    num = 0
    x = -1
    y = 0
    step = 1
    size = n
    
    while size > 0:
        for _ in range(size):
            x += step
            num += 1
            arr[y][x] = num
        size -= 1
        
        for _ in range(size):
            y += step
            num += 1
            arr[y][x] = num
        step *= -1
    print(f'#{test_case}')
    for i in arr:
        print(*i)