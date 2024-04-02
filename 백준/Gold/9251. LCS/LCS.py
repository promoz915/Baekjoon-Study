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