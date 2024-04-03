import sys; input = sys.stdin.readline

n = int(input())
m = []
d = [[-1 for j in range(n+1)] for i in range(n+1)]

m.append((0, 0))

for i in range(n):
    a, b = map(int, input().split())
    m.append((a, b))

def mul(s, e):
    result = sys.maxsize
    if d[s][e] != -1:       # 메모이제이션
        return d[s][e]
    # 행렬 1개의 곱셈 연산
    if s == e:
        return 0
    # 행렬 2개의 곱셈 연산
    if s + 1 == e:
        return m[s][0] * m[s][1] * m[e][1]
    # 행렬 3개의 곱셈 연산
    for i in range(s, e):
        # a = s 행렬 row * i 행렬 col(i+1 행렬 row와 같음) * e 행렬 col
        result = min(result, m[s][0] * m[i][1] * m[e][1] + mul(s, i) + mul(i + 1 , e))
    d[s][e] = result
    return d[s][e]

print(mul(1, n))