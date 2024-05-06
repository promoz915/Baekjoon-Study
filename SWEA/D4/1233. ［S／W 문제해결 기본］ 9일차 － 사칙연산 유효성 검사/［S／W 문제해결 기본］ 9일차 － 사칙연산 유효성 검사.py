def check(s):
    if s == '+' or s == '-' or s == '*' or s == '/':
        return True
    return False


for test_case in range(1, 11):
    n = int(input())
    temp = n//2
    ans = 1
    
    for i in range(n):
        data = input().split()
        num = int(data[0])
        order = data[1]
        
        if num <= temp:
            if not check(order):
                ans = 0
        else:
            if check(order):
                ans = 0
                
    print(f'#{test_case} {ans}')