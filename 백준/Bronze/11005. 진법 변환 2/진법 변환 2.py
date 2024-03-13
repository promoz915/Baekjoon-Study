a, b = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while a:
    s += str(arr[a%b])
    a //= b
print(s[::-1])