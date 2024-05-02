def solution(n):
    temp = pow(n, 0.5)
    return pow(temp+1, 2) if temp == int(temp) else -1