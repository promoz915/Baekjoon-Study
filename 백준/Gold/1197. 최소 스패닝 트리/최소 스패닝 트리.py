import sys
from queue import PriorityQueue
input = sys.stdin.readline

n, m = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for i in range(m):
    s, e, w = map(int, input().split())
    pq.put((w, s, e))                   # 가중치를 제일 앞으로

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < n-1:                    # 항상 n-1의 에지를 사용
    w, s, e = pq.get()
    if find(s) != find(e):              # 같은 부모가 아닌 경우만 연결
        union(s, e)
        result += w
        useEdge += 1

print(result)