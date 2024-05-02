def solution(x):
    cnt = 0
    temp = x
    while temp:
        cnt += temp % 10
        temp //= 10
    return True if x % cnt == 0 else False