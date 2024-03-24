import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
m = int(input())
myList = [[] for _ in range(n+1)]
dist = [sys.maxsize] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    s, e, w = map(int,input().split())
    myList[s].append((e, w))

start, end = map(int, input().split())

def dijkstra(s, e):
    pq =  PriorityQueue()
    pq.put((0, s))
    dist[s] = 0

    while pq.qsize() > 0:
        nowNode = pq.get()
        now = nowNode[1]
        if not visited[now]:
            visited[now] = True
            for n in myList[now]:
                if not visited[n[0]] and dist[n[0]] > dist[now] + n[1]:
                    dist[n[0]] = dist[now] + n[1]
                    pq.put((dist[n[0]], n[0]))

    return dist[e]

print(dijkstra(start, end))