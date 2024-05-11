import sys
input = sys.stdin.readline

def check(a, ans, t):
    while a > 0:
        ans[a % 10] += t
        a //= 10


ans = [0] * 10
start = 1
end = int(input())
mul = 1

while start <= end:
    while start % 10 != 0 and start <= end:
        check(start, ans, mul)
        start += 1
    if start > end or (start == 0 and end == 0):
        break
    while end % 10 != 9 and start <= end:
        check(end, ans, mul)
        end -= 1

    start //= 10
    end //= 10

    for i in range(10):
        ans[i] += (end - start + 1) * mul
    mul *= 10

for i in range(10):
    print(ans[i], end=' ')