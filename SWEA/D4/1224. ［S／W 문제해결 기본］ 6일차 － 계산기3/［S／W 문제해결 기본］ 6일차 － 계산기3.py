for test_case in range(1, 11):
    n = int(input())
    calc = list(input())
    
    result = []
    stack = []
    
    dct_1 = {'*': 2, '+': 1, '(': 0}
    dct_2 = {'*': 2, '+': 1, '(': 3}
    
    for i in calc:
        if i in '0123456789':
            result.append(i)
        elif i in '*+(':
            if not stack:
                stack.append(i)
            else:
                if dct_1[stack[-1]] >= dct_2[i]:
                    while stack and dct_1[stack[-1]] >= dct_2[i]:
                        result.append(stack.pop())
                stack.append(i)
        else:
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
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
            