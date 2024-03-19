import sys; input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n)]
visited = [False] * n
d = [0] * n
lcm = 1

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

def DFS(v):
    visited[v] = True
    for i in arr[v]:
        next = i[0]
        if not visited[next]:               # 현재 노드의 연결 노드 중 방문하지 않은 노드
            d[next] = d[v] * i[2] // i[1]   # 다음 노드의 값 = 현재 노드의 값 * 비율
            DFS(next)                       # 재귀함수

for i in range(n-1):
    a, b, p, q = map(int, input().split())
    arr[a].append((b, p, q))
    arr[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))             # 최소공배수 업데이트

d[0] = lcm                                  # 0번 노드에 최소공배수 저장
DFS(0)
mgcd = d[0]

for i in range(1, n):                       # 업데이트 된 d 리스트 값들의 최대공약수 계산
    mgcd = gcd(mgcd, d[i])

for i in range(n):                          # d 리스트의 각 값을 최대공약수로 나눠 출력
    print(int(d[i] // mgcd), end=' ')