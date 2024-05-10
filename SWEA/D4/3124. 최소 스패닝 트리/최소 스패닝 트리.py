from queue import PriorityQueue

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    pq = PriorityQueue()
    parent = [0] * (n+1)
    
    for i in range(n+1):
        parent[i] = i
        
    for i in range(m):
        s, e, w = map(int, input().split())
        pq.put((w, s, e))
        
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
            
    use_edge = 0
    ans = 0
    
    while use_edge < n-1:
        w, s, e = pq.get()
        if find(s) != find(e):
            union(s, e)
            ans += w
            use_edge += 1
    
    print(f'#{test_case} {ans}')