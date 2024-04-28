a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = max(sum(a), sum(b))
print(ans)