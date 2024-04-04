T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    a_p = 0
    a_q = 0
    
    for i in range(200):
        if p > 0:
            p = p - i
            a_p = i
        if q > 0:
            q = q - i
            a_q = i
    p_x = a_p + p
    p_y = abs(p) + 1
    q_x = a_q + q
    q_y = abs(q) + 1
    result_x = p_x + q_x
    result_y = p_y + q_y
    result = 0
    temp = result_x + result_y
    for i in range(temp-1):
        result += i
    result += result_x
    print(f'#{test_case} {result}')