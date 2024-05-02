def solution(num):
    cnt = 0
    while num != 1:
        if num % 2:
            num = num * 3 + 1
            cnt += 1
        else:
            num //= 2
            cnt += 1
    return cnt if cnt < 500 else -1