def pal(word):
    n = len(word)
    if word == word[::-1]:
        if word[:n//2] == word[:n//2][::-1] and word[n//2+1:] == word[n//2+1:][::-1]:
            return 'YES'
        else: return 'NO'
    return 'NO'

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    words = input()
    ans = pal(words)
    print(f'#{test_case} {ans}')