import sys; input = sys.stdin.readline

n = int(input())
ans = 0
people = set()

for i in range(n):
    word = input().rstrip()
    if word == "ENTER":
        ans += len(people)
        people = set()
    else:
        people.add(word)

print(ans + len(people))