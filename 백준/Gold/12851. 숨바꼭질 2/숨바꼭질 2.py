import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
MOD = 100001
a = [0] * MOD
cnt = 0
result = 0


def bfs():
    global cnt, result
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        temp = a[x]
        if x == k:
            result = temp
            cnt += 1
            continue

        for i in (x-1, x+1, x*2):
            if 0 <= i < MOD and (a[i] == 0 or a[i] == a[x] + 1):
                a[i] = a[x] + 1
                queue.append(i)

bfs()
print(result)
print(cnt)