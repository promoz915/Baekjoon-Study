for test_case in range(1, 11):
    n = int(input())
    data = list(map(str, input()))
    stack = []
    
    left = ['(', '{', '[', '<']
    right = [')', '}', ']', '>']
    
    for i in range(n):
        if data[i] in left:
            stack.append(data[i])
        
        elif data[i] in right:
            if right.index(data[i]) == left.index(stack[-1]):
                stack.pop()
            else:
                break
    ans = 0
    if len(stack) == 0:
        ans = 1
    print(f'#{test_case} {ans}')