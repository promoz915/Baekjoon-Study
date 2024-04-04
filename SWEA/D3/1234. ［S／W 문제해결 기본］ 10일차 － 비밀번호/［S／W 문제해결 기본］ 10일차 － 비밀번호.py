T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = input().split()
    stack = [m[0]]
    
    for i in range(1, int(n)):
        if len(stack) != 0 and stack[-1] == m[i]:
            stack.pop()
        else:
            stack.append(m[i])
    print(f"#{test_case} {''.join(map(str, stack))}")