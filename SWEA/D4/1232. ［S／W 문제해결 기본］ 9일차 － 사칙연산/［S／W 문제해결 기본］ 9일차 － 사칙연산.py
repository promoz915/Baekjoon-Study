def func(num):
    if len(tree[num]) == 2:
        return int(tree[num][1])
    else:
        left = func(int(tree[num][2]))
        right = func(int(tree[num][3]))
        
        if tree[num][1] == '+':
            return left + right
        elif tree[num][1] == '-':
            return left - right
        elif tree[num][1] == '*':
            return left * right
        else:
            return left / right
        

for test_case in range(1, 11):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    for _ in range(n):
        data = input().split()
        tree[int(data[0])] = data
   
    print(f'#{test_case} {int(func(1))}')