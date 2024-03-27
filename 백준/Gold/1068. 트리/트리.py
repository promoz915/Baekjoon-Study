import sys; sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
visited = [False] * n
tree = [[] for _ in range(n)]
ans = 0
p = list(map(int, input().split()))

for i in range(n):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

def dfs(num):
    global ans
    visited[num] = True
    cNode = 0
    for i in tree[num]:
        if not visited[i] and i != deleteNode:
            cNode += 1
            dfs(i)
    if cNode == 0:
        ans += 1

deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    dfs(root)
    print(ans)