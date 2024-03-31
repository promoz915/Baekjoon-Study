import sys; input = sys.stdin.readline

f = [0] * 21            # 팩토리얼 리스트
s = [0] * 21            # 순열 리스트
visited = [False] * 21
n = int(input())
f[0] = 1

# 팩토리얼 초기화
for i in range(1, n+1):
    f[i] = f[i-1] * i

arr = list(map(int, input().split()))

# 순열을 출력하는 문제
if arr[0] == 1:
    k = arr[1]      # 몇 번째 순열을 출력할 지 입력
    for i in range(1, n+1):
        cnt = 1     # 해당 자리에서 몇 번째 숫자를 사용해야 할지를 정하는 변수
        for j in range(1, n+1):
            if visited[j]:                  # 이미 사용한 숫자는 패스
                continue
            if k <= cnt * f[n-i]:           # 주어진 k에 따라 각 자리에 들어갈 수 있는 수 찾기
                k -= (cnt - 1) * f[n-i]
                s[i] = j                    # 순열 리스트에 추가
                visited[j] = True           # 사용된 숫자로 체크
                break
            cnt += 1                        # if문에 들어가지 못하면 cnt 늘리기
    for i in range(1, n+1):
        print(s[i], end=' ')

# 순열의 순서를 출력하는 문제
else:
    k = 1
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, arr[i]):
            if not visited[j]:              # 사용한 숫자가 아니면
                cnt += 1                    # 건너뛴 미사용 숫자 1 증가
        k += cnt * f[n - i]                 # 자릿수에 따라 순서 정하기
        visited[arr[i]] = True              # 사용된 숫자로 체크
    print(k)