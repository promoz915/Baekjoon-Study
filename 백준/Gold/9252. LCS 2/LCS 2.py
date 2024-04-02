import sys; sys.setrecursionlimit(10000)
input = sys.stdin.readline

a = list(input())
a.pop()
b = list(input())
b.pop()
arr = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
path = []

# LCS 길이 산출
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            # 같은 문자열일 때 왼쪽 대각선 값 + 1
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            # 다르면 왼쪽과 위의 값 중 큰 수
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])

print(arr[len(a)][len(b)])

# LCS 문자열 산출
def lcs(n, m):
    if n == 0 or m == 0:
        return
    if a[n - 1] == b[m - 1]:
        # 문자열이 같으면 path에 append 하고 왼쪽 위로 이동
        path.append(a[n - 1])
        lcs(n - 1, m - 1)
    else:
        # 다르면 왼쪽 값과 위의 값 중 값이 더 큰 쪽으로 이동
        if arr[n - 1][m] > arr[n][m - 1]:
            lcs(n - 1, m)
        else:
            lcs(n, m - 1)
            
lcs(len(a), len(b))

for i in range(len(path)-1, -1, -1):
    print(path.pop(i), end='')
print()