from collections import deque

n, k = map(int, input().split())
MAX = (10 ** 5) * 2
a = [0] * (MAX+1)
def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(a[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= MAX and not a[i]:
                a[i] = a[x] + 1
                queue.append(i)
bfs()
