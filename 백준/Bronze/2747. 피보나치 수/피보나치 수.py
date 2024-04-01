import sys; input = sys.stdin.readline

n = int(input())
d = [-1] * (n+1)
d[0] = 0
d[1] = 1

def fibo(n): 
    if d[n] != -1:                  # 기존에 계산한 적이 있는 부분의 문제는 재계산하지 않고 리턴
        return d[n]
    # 메모이제이션: 구한 값을 바로 리턴하지 않고 dp 테이블에 저장한 후 리턴하도록 로직 구현
    d[n] = fibo(n-2) + fibo(n-1)
    return d[n]

fibo(n)
print(d[n])