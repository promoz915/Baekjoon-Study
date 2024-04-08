n = int(input())

def func(num):
    result = 0
    for i in num:
        if i.isdigit():
            result += int(i)
    return result

a = []
for i in range(n):
    word = input()
    a.append(word)

a.sort(key=lambda x:(len(x), func(x), x))
for i in a:
    print(i)