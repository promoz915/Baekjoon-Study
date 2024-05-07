def func(num):
    global word
    if num <= n:
        func(num * 2)
        word += data[num-1][1]
        func(num * 2 + 1)


for test_case in range(1, 11):
    n = int(input())
    data = [input().split() for _ in range(n)]
    word = ''
    func(1)
    print(f'#{test_case} {word}')