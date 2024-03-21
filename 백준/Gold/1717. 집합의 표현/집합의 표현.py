import sys; sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n + 1)

def find(a):
    if a == parent[a]:
        return a                    # 대표 노드면 리턴
    else:
        parent[a] = find(parent[a]) # 아니면 a의 대표 노드값을 find(parent[a])값으로 저장(재귀함수)
        return parent[a]

def union(a, b):                    # union 연산 대표 노드끼리 합치기
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):                # 두 원소가 같은 집합에 속해 있는지 확인하는 함수
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(0, n+1):
    parent[i] = i                   # 대표 노드를 자기 자신으로 초기화

for i in range(m):
    question, a, b = map(int, input().split())
    if question == 0:               # 맨 앞 숫자가 0이면
        union(a, b)                 # union 연산
    else:
        if checkSame(a, b):         # 아니면 checkSame 연산
            print("YES")
        else:
            print("NO")