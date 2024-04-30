def solution(n):
    a = [False, False] + [True] * (n-1)
    prime = []
    
    for i in range(2, n+1):
        if a[i]:
            prime.append(i)
            for j in range(i+i, n+1, i):
                a[j] = False
    return len(prime)