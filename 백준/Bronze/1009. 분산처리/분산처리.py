import sys
input = sys.stdin.readline

a = int(input())
for _ in range(a):
    n, m = map(int, input().split())
    num = n % 10

    if num == 0:
        print(10)
    elif num in [1, 5, 6]:
        print(num)
    elif num in [4, 9]:
        num2 = m % 2
        if num2 == 0:
            print(num * num % 10)
        else:
            print(num)
    else:
        num2 = m % 4
        if num2 == 0:
            print(num ** 4 % 10)
        else:
            print(num ** num2 % 10)