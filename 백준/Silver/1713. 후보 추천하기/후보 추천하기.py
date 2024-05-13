import sys
input = sys.stdin.readline

n = int(input())
vote = int(input())
vote_list = list(map(int, input().split()))

ans, cnt = [], []

for i in vote_list:
    if i in ans:
        cnt[ans.index(i)] += 1
    else:
        if len(ans) >= n:
            idx = cnt.index(min(cnt))
            del ans[idx]
            del cnt[idx]
        ans.append(i)
        cnt.append(1)

ans.sort()
print(' '.join(map(str, ans)))