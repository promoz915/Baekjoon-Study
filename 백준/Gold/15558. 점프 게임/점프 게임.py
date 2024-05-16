import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
left = list(map(int, input().rstrip()))
right = list(map(int, input().rstrip()))
data = [left, right]

visited_left = [0 for _ in range(n)]
visited_right = [0 for _ in range(n)]
visited = [visited_left, visited_right]
visited[0][0] = True

def bfs():
    idx = 0
    queue = deque()
    queue.append([idx, 0, 0])
    
    while queue:
        idx, pos, time = queue.popleft()
        dx = [1, -1, k]
        
        for j in range(3):
            nx = idx + dx[j]
            
            if nx >= n:
                return print(1)
            
            if time < nx and data[pos][nx] == 1 and j != 2:
                if not visited[pos][nx]:
                    visited[pos][nx] = True
                    queue.append((nx, pos, time + 1))
            
            elif time < nx and data[1 - pos][nx] == 1 and j == 2:
                if not visited[1 - pos][nx]:
                    visited[1 - pos][nx] = True
                    queue.append((nx, 1 - pos, time + 1))
                    
    print(0)
bfs()
                    