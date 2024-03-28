import sys; input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

max_num = - int(1e9)
min_num = int(1e9)

def dfs(add, sub, mul, div, sum, idx):
    global max_num, min_num

    if idx == n:
        max_num = max(max_num, sum)
        min_num = min(min_num, sum)
        return
    if add:
        dfs(add - 1, sub, mul, div, sum + num[idx], idx + 1)
    if sub:
        dfs(add, sub - 1, mul, div, sum - num[idx], idx + 1)
    if mul:
        dfs(add, sub, mul - 1, div, sum * num[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div - 1, int(sum / num[idx]), idx + 1)

dfs(add, sub, mul, div, num[0], 1)
print(max_num)
print(min_num)