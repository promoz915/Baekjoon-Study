def check(words):
    check_list = 'abcdefghijklmnopqrstuvwxyz'
    words = list(set(words))

    cnt = 0
    for c in check_list:
        if c in words:
            cnt += 1
    if cnt == 26:
        return True
    return False

def dfs(idx, depth, words):
    global ans

    if check(words):
        ans += 1

    if depth == n:
        return

    for i in range(idx, n):
        dfs(i+1, depth+1, words+data[i])

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    data = [input() for _ in range(n)]
    ans = 0
    dfs(0, 0, '')
    print(f'#{test_case} {ans}')