target = ['a', 'e', 'i', 'o', 'u']
ans = 0
word = input()
for w in word:
    if w in target:
        ans += 1
print(ans)