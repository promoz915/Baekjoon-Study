def put(idx, left, right, p):
    global n, ans, sum_data
    
    if idx == n:
        ans += 1
        return
    
    if left > sum_data // 2:
        temp = n - idx
        ans += (2 ** temp)
        return
    
    put(idx + 1, left + p[idx], right, p)
    if right + p[idx] <= left:
        put(idx + 1, left, right + p[idx], p)


def perm(length, now, remaining):
    if length == n:
        put(0, 0, 0, now)
        return
    for i in range(len(remaining)):
        perm(length + 1, now + [remaining[i]], remaining[:i] + remaining[i+1:])

        
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    data = list(map(int, input().split()))
    sum_data = sum(data)
    ans = 0
    perm(0, [], data)
    print(f'#{test_case} {ans}')