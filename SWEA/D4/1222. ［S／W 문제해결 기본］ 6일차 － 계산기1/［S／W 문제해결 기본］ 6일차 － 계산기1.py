for test_case in range(1, 11):
    n = int(input())
    data = list(input())

    result = []
    stack = []

    for i in data:
        if i == '+':
            while stack:
                result.append(stack.pop())
            stack.append(i)
        else:
            result.append(i)

    while stack:
        result.append(stack.pop())

    ans = []
    for i in result:
        if i == '+':
            ans.append(ans.pop() + ans.pop())
        else:
            ans.append(int(i))

    print(f'#{test_case} {ans[-1]}')