def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def check(a, b):
    return find(a) == find(b)


t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    ans = []
    for _ in range(m):
        n, a, b = map(int, input().split())
        if n == 0:
            union(a, b)
        else:
            ans.append(str(1 if check(a, b) else 0))
    print(f'#{test_case} {"".join(ans)}')