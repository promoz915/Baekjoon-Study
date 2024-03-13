import sys; input = sys.stdin.readline

def fib(n):
    zero = [1, 0, 1]    # n이 0이면 1, n이 1이면 0, n이 2이면 1
    one = [0, 1, 1]     # n이 0이면 0, n이 1이면 1, n이 2이면 1
    if n >= 3:
        for i in range(2, n):
            zero.append(zero[i-1] + zero[i])
            one.append(one[i-1] + one[i])
    print(zero[n], one[n], sep=' ')

t = int(input())
for _ in range(t):
    n = int(input())
    fib(n)