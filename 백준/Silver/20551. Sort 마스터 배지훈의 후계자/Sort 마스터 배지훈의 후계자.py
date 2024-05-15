import sys
input = sys.stdin.readline

def func(num, target):
    left, right = 0, len(num) - 1
    while left <= right:
        mid = (left + right) // 2
        if num[mid] < target:
            left = mid + 1
        elif num[mid] > target:
            right = mid - 1
        elif num[mid] == target:
            if right == mid:
                break
            right = mid

    if num[mid] == target:
        return mid
    else:
        return -1


n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
ans = []

for i in range(m):
    q = int(input())
    ans.append(func(a, q))

for an in ans:
    print(an)