import sys
input = sys.stdin.readline

t = int(input())

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a * b / gcd(a,b)

for i in range(t):
    a, b = map(int, input().split())
    print(int(lcm(a, b)))