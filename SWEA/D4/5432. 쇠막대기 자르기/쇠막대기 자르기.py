t = int(input())
for test_case in range(1, t+1):
    data = list(map(str, input()))
    stack = []
    cnt = 0
    
    for i in range(len(data)):
        if data[i] == '(':
            stack.append('(')
        elif data[i] == ')':
            if data[i-1] == '(':
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
    print(f'#{test_case} {cnt}')