n = int(input())
def five(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt
print(five(n))