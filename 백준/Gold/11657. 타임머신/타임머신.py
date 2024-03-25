import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
distance = [sys.maxsize] * (n+1)

for i in range(m):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

distance[1] = 0

for _ in range(n-1):
    for s, e, w in edges:
        if distance[s] != sys.maxsize and distance[e] > distance[s] + w:
            distance[e] = distance[s] + w
            
# 음수 사이클
mCycle = False

for s, e, w in edges:
    if distance[s] != sys.maxsize and distance[e] > distance[s] + w:
        mCycle = True

if not mCycle:
    for i in range(2, n+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)