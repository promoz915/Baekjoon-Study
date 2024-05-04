for test_case in range(1, 11):
    n = int(input())
    data = list(input())
    
    result = []
    stack = []
    
    dct = {'*': 2, '+': 1}
    
    for i in data:
        if i != '*' and i != '+':
            result.append(i)
        else:
            if not stack:
                stack.append(i)
            else:
                if dct[stack[-1]] >= dct[i]:
                    while stack and dct[stack[-1]] >= dct[i]:
                        result.append(stack.pop())
                stack.append(i)
                
    while stack:
        result.append(stack.pop())
        
    ans = []
    i = 0
    
    for i in result:
        if i != '*' and i != '+':
            ans.append(i)
        elif i == '*':
            ans[-2] = int(ans[-2]) * int(ans[-1])
            ans.pop()
        else:
            ans[-2] = int(ans[-2]) + int(ans[-1])
            ans.pop()
     
    print(f'#{test_case} {ans[0]}')