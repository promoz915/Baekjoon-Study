import sys
input = sys.stdin.readline

def count_visited(arr, start):
    visited = [0] * (n+1)
    stack = [start]
    while stack:
        now = stack.pop()
        for next in arr[now]:
            if not visited[next]:
                visited[next] = 1
                stack.append(next)

    return visited.count(1)


n, m = map(int, input().split())

num_in = [[] for _ in range(n+1)]
num_out = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    num_in[b].append(a)
    num_out[a].append(b)

cnt = 0
for stdnt in range(1, n+1):
    if count_visited(num_in, stdnt) + count_visited(num_out, stdnt) == n-1:
        cnt += 1

print(cnt)