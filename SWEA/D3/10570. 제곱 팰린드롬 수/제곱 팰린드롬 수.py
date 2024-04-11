import math

def pal(num):
    return str(num) == str(num)[::-1]

t = int(input())
for test_case in range(1, t + 1):
    a, b = map(int, input().split())
    ans = 0

    for i in range(a, b+1):
        if pal(i):
            temp = math.sqrt(i)
            if temp == int(temp) and pal(int(temp)):
                ans += 1

    print(f'#{test_case} {ans}')