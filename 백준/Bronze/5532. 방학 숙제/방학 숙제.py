l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = a // c
y = b // d

if x > y:
    if a % c == 0:
        print(l - x)
    else:
        print(l - x - 1)
else:
    if b % d == 0:
        print(l - y)
    else:
        print(l - y - 1)