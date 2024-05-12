from collections import Counter


def check(word, words):
    for w in words:
        if w not in word or word[w] == 0:
            return False
        else:
            word[w] -= 1
    return True


t = input()
n = int(input())
books = []
for _ in range(n):
    price, title = input().split()
    books.append((int(price), Counter(title)))

ans = 1e9

for i in range(1<<n):
    price = 0
    word = Counter()
    
    for j in range(n):
        if (i & 1 << j) != 0:
            price += books[j][0]
            word += books[j][1]
            
    if check(word, t):
        ans = min(ans, price)
        
print(-1) if ans == 1e9 else print(ans)